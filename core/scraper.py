import requests
from bs4 import BeautifulSoup

def get_src(url):
    response = requests.get(url)
    domen = "https://books.toscrape.com/"
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("h1").get_text()
        price = soup.find("p", class_="price_color").get_text()[2:]
        img = domen + soup.find("img").get('src').replace('../', '')
        article = soup.find("article", class_="product_page").find_all("p")[3]
        description = article.get_text()
        return [title, price, img, description]

# domen = "https://books.toscrape.com/"
# response = requests.get("http://books.toscrape.com/")
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     articles = soup.find_all("article", class_="product_pod")
#     for article in articles:
#         link = domen+article.find("a").get('href')
#         print(get_src(link))
# else:
#     print("Failed to retrieve the website.")



