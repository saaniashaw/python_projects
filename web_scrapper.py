import requests
from bs4 import BeautifulSoup
import csv

def scrape_products(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.product-item'):  # Adjust selector based on the website structure
        name = item.select_one('.product-name').text
        price = item.select_one('.product-price').text
        products.append({'name': name, 'price': price})

    return products

def save_to_csv(products, filename='products.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(products)

if __name__ == '__main__':
    url = 'https://example-ecommerce-site.com'  # Replace with the actual URL
    products = scrape_products(url)
    save_to_csv(products)
    print(f"Scraped {len(products)} products and saved to products.csv.")
