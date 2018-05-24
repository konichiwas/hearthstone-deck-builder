import random

from .models import Card

def split_cards(cards, step):
	all_ = []
	for i in range(0, len(cards), step):
	    chunk = cards[i:i+step]
	    all_.append(chunk)
	return all_

def get_random_card(expansion):
	cards = Card.objects.filter(expansion__name=expansion)
	card = random.choice(cards)
	return card.image_gold