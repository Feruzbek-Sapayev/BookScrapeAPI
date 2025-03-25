from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from core.models import Book

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
        return {'title': title, 'price': price, 'image': img, 'description': description}

class Command(BaseCommand):
    help = "Saytdan ma'lumotlarni yig'ib olish (scraping)"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Scraping started...'))

        domen = "https://books.toscrape.com/"
        response = requests.get("http://books.toscrape.com/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article", class_="product_pod")
            for article in articles:
                link = domen+article.find("a").get('href')
                content = get_src(link)
                obj, created = Book.objects.get_or_create(title=content['title'], price=content['price'], image=content['image'], description=content['description'])
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Saved: {content['title']}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Already exists: {content['title']}"))
            self.stdout.write(self.style.SUCCESS(f"Scraping finished! {len(articles)} content saved!"))
        else:
            print("Failed to retrieve the website.")




