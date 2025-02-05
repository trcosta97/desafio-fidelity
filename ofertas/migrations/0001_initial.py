# Generated by Django 5.1.5 on 2025-02-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.URLField()),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parcelamento', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField()),
                ('preco_sem_desconto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('percentual_desconto', models.CharField(blank=True, max_length=10, null=True)),
                ('tipo_entrega', models.CharField(max_length=10)),
                ('frete_gratis', models.BooleanField()),
            ],
        ),
    ]
