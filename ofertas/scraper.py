import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def safe_find_element(item, by, selector, attribute=None, default=''):
    try:
        element = item.find_element(by, selector)
        if attribute:
            return element.get_attribute(attribute) or default
        return element.text if hasattr(element, 'text') else element
    except:
        return default

def scrape_mercado_livre():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://www.mercadolivre.com.br')
        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'as_word'))
        )
        search_box.send_keys('Computador Gamer i7 16gb ssd 1tb')
        search_box.submit()
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.poly-card__content'))
        )

        items = driver.find_elements(By.CSS_SELECTOR, '.poly-card')
        products = []

        for item in items:
            try:
                product = {
                    'image': safe_find_element(item, By.CSS_SELECTOR, '.poly-component__picture', attribute='src'),
                    'name': safe_find_element(item, By.CSS_SELECTOR, '.poly-component__title').text,
                    'price': safe_find_element(item, By.CSS_SELECTOR, '.poly-price__current .andes-money-amount__fraction').text,
                    'installments': safe_find_element(item, By.CSS_SELECTOR, '.poly-price__installments').text,
                    'link': safe_find_element(item, By.CSS_SELECTOR, '.poly-component__title', attribute='href'),
                    'original_price': safe_find_element(item, By.CSS_SELECTOR, '.andes-money-amount--previous .andes-money-amount__fraction', multiple=False).text if safe_find_element(item, By.CSS_SELECTOR, '.andes-money-amount--previous', multiple=False) else None,
                    'discount': safe_find_element(item, By.CSS_SELECTOR, '.poly-price__current .andes-money-amount__discount').text if safe_find_element(item, By.CSS_SELECTOR, '.andes-money-amount__discount', multiple=False) else None,
                    'delivery_type': 'Full' if safe_find_element(item, By.CSS_SELECTOR, '.poly-component__shipped-from') else 'Normal',
                    'free_shipping': 'Sim' if safe_find_element(item, By.CSS_SELECTOR, '.poly-component__shipping') else 'Não',
                    'reviews_rating': safe_find_element(item, By.CSS_SELECTOR, '.poly-reviews__rating').text,
                    'reviews_count': safe_find_element(item, By.CSS_SELECTOR, '.poly-reviews__total').text.strip('()')
                }
                products.append(product)
            except Exception as e:
                print(f"Erro ao extrair item: {e}")

        return products

    except Exception as e:
        print(f"Erro no scraping: {e}")
        return []

    finally:
        driver.quit()

def safe_find_element(parent, by, selector, attribute=None, multiple=True):
    try:
        if multiple:
            elements = parent.find_elements(by, selector)
            if elements:
                return elements[0].get_attribute(attribute) if attribute else elements[0]
        else:
            element = parent.find_element(by, selector)
            return element.get_attribute(attribute) if attribute else element
    except Exception:
        return None

# Exemplo de uso
if __name__ == "__main__":
    data = scrape_mercado_livre()
    for d in data:
        print(d)
