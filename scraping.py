import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_mystery_books():
    data = []
    base_url = "https://books.toscrape.com/catalogue/category/books/mystery_3/"
    page_urls = ["index.html", "page-2.html"]

    for page in page_urls:
        url = base_url + page
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            # Title
            title = article.h3.a['title']
            # Price
            price = article.find('p', class_='price_color').get_text(strip=True)
            # Star rating
            star = article.find('p', class_='star-rating')['class'][1]
            data.append({"Title": title, "Price": price, "Star": star})

    return pd.DataFrame(data)

df = scrape_mystery_books()
print(df)