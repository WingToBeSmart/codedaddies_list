import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
# Create your views here.

BASE_CRAIGSLIST_URL = 'https://hongkong.craigslist.org/search/?query={}'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    # print(data)
    stuff_for_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
