from django.shortcuts import render

from .card_filter import SearchForm
from .models import Card, New, Promo, PlayerClass
from .utils import split_cards, get_random_card
from .contactform import ContactForm

def index(request):
	cards = {}
	promos = Promo.objects.all()
	news = New.objects.all().order_by('-date')
	for promo in promos:
		key = promo.expansion.name
		cards[key] = get_random_card(promo)
	context = {
		'promos': promos,
		'news': news,
		'cards': cards,
	}
	return render(request, 'builder/index.html', context)

def album(request):
	form = SearchForm(request.GET or None)
	if form.is_valid():
		cards = form.get_data()
	else:
		cards = Card.objects.all().order_by('cost')
	
	classes = PlayerClass.objects.all().exclude(name="Neutral")
	context = {
		'cards': split_cards(cards, 8),
		'form': form,
		'classes': classes,  
	}	
	return render(request, 'builder/album.html', context)

def contact(request):
	form =  ContactForm(request.POST or None, label_suffix='')
	success = False
	if form.is_valid():
		form.save()
		success = True
		form = ContactForm()
	context = {
		'form': form,
		'success': success,
	}
	return render(request, 'builder/contact.html', context)