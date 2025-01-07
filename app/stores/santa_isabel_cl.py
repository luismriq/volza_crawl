import requests
from bs4 import BeautifulSoup

def fetch_product_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        # Extraer datos del producto
        product_name = soup.find('h1', class_='product-name').text.strip()
        price = soup.find('span', class_='price').text.strip()
        nutrition_info = soup.find('div', class_='nutrition-info').text.strip()
        technical_info = soup.find('div', class_='technical-info').text.strip()
        
        return {
            'name': product_name,
            'price': price,
            'nutrition_info': nutrition_info,
            'technical_info': technical_info
        }
    else:
        print(f"Error fetching data from {url}")
        return None

if __name__ == "__main__":
    url = 'URL_DEL_PRODUCTO_EN_SANTA_ISABEL'
    product_data = fetch_product_data(url)
    if product_data:
        print(product_data)
