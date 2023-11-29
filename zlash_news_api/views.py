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
