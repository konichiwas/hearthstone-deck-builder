import urllib.parse

from django.shortcuts import render
from django.core.paginator import Paginator

from .card_filter import SearchForm
from .models import Card

def index(request):
	return render(request, 'builder/index.html')

def main(request):
	form = SearchForm(request.GET or None)
	if form.is_valid():
		cards, params = form.get_data()
	else:
		cards = Card.objects.all().order_by('cost')
		params = {}	
	url = urllib.parse.urlencode(params)

	paginator = Paginator(cards, 14)
	page = request.GET.get('page')
	results = paginator.get_page(page)
	
	context = {
		'cards': results,
		'form': form,  
		'url': url,
	}	
	return render(request, 'builder/main.html', context)