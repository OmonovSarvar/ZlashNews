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
        url1 = 'https://www.bbc.com/news'  # Get news from this links
        url2 = 'https://eurasianet.org'  # Get news from this links

        # request to first site
        news_list = []
        response = requests.get(url1)
        soup = BeautifulSoup(response.content, 'html.parser')
        result = soup.find(id='orb-modules')
        title = result.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')
        content = result.find_all('p', class_='gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
