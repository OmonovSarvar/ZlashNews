# Build In packages
from calendar import weekday, day_name
from datetime import date

# Third party package
import requests
from bs4 import BeautifulSoup
from rest_framework import generics

# Local application
from .models import NewsModel
from .serializers import NewsSerializer


class NewsList(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        # Get day of the week
        day = date.today()
        x = day_name[day.weekday()]

        url1 = 'https://www.bbc.com/news'  # Get news from this links
        url2 = 'https://eurasianet.org'  # Get news from this links

        # request to first site
        news_list = []
        response = requests.get(url1)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find(id='orb-modules')
        title = result.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
        content = result.find_all('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
        title = title[:15]
        content = content[:15]
        for i in range(1, 15, 2):
            piece_title = title[i: i + 2]
            piece_content = content[i: i + 2]
            for main, cont in piece_title, piece_content:
                main = main.text
                cont = cont.text
                if not NewsModel.objects.filter(title=main).exists():
                    model = NewsModel(title=main, description=cont, url=url1, day=x)
                    model.save()
                    news_list.append(model)
                else:
                    model = NewsModel(title=main, description=cont, url=url1, day=x)
                    news_list.append(model)
        # Request to eurasia net
        response = requests.get(url2)
        soup_second = BeautifulSoup(response.content, 'html.parser')
        result_two = soup.find(id='orb-modules')
        title_two = result_two.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
        content_two = result_two.find_all('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
        title_two = title_two[0:16]
        content_two = content_two[0:16]
        for i in range(0, 16, 2):
            piece_title_two = title_two[i: i + 2]
            piece_content_two = content_two[i: i + 2]
            for tit, cont2 in piece_title_two, piece_content_two:
                tit = tit.text
                cont2 = cont2.text
                if not NewsModel.objects.filter(title=tit).exists():
                    model = NewsModel(title=tit, description=cont2, url=url2, day=x)
                    model.save()
                    news_list.append(model)
                else:
                    model = NewsModel(title=tit, description=cont2, url=url2, day=x)
                    news_list.append(model)
        return news_list
