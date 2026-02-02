import requests
from bs4 import BeautifulSoup

def find_quotes():
    for page in range(1, 10+1):
        print("=" * 50)
        print(f"Page {page}")
        print("=" * 50)

        soup = BeautifulSoup(
            requests.get(f"https://quotes.toscrape.com/page/{page}/").text,
            "html.parser"
        )

        for q in soup.select(".quote"):
            print(q.select_one(".text").text)
            print("—", q.select_one(".author").text)
            print("-" * 50)

# find_quotes()

def find_book():
    for page in range(1, 50+1):
        print("=" * 35)
        print(f"Page {page}")
        print("=" * 35)

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price = book.select_one("p.price_color").text
            stock = book.select_one("p.instock.availability").get_text(strip=True)

            print(title)
            print(price)
            print(stock)
            print("-" * 40)

find_book()