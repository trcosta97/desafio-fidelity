from django.shortcuts import render
from .models import Produto
from .scraper import scrape_mercado_livre
from decimal import Decimal, InvalidOperation

def listar_produtos(request):
    Produto.objects.all().delete()
    
    produtos_ml = scrape_mercado_livre()
    
    produtos_filtrados = []
    for produto in produtos_ml:
        try:
            novo_produto = Produto.objects.create(
                nome=produto['name'] or '',
                preco=safe_decimal(produto['price']) or 0,
                imagem=produto['image'] or '',
                link=produto['link'] or '',
                parcelamento=produto['installments'] or '',
                preco_sem_desconto=safe_decimal(produto['original_price']) or 0,
                percentual_desconto=produto['discount'] or '',
                tipo_entrega=produto['delivery_type'] or '',
                frete_gratis=produto['free_shipping'] == 'Sim'
            )
            if (request.GET.get('frete_gratis') == 'true' and produto['free_shipping'] == 'Sim') or \
               (request.GET.get('full') == 'true' and produto['delivery_type'] == 'Full') or \
               (not request.GET.get('frete_gratis') and not request.GET.get('full')):
                produtos_filtrados.append(novo_produto)
        except Exception as e:
            print(f"Erro ao criar produto: {e}")
    
    if produtos_filtrados:
        menor_preco = min(produtos_filtrados, key=lambda x: x.preco)
        maior_preco = max(produtos_filtrados, key=lambda x: x.preco)
        maior_desconto = max(produtos_filtrados, key=lambda x: safe_decimal(x.percentual_desconto.rstrip('%')))
    else:
        menor_preco = maior_preco = maior_desconto = None

    return render(request, 'ofertas/lista.html', {
        'produtos': produtos_filtrados,
        'menor_preco': menor_preco,
        'maior_preco': maior_preco,
        'maior_desconto': maior_desconto
    })


def safe_decimal(value):
    try:
        cleaned_value = ''.join(char for char in str(value) if char.isdigit() or char == '.')
        return Decimal(cleaned_value) if cleaned_value else Decimal('0')
    except (InvalidOperation, ValueError):
        return Decimal('0')
