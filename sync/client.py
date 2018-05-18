import requests

from django.conf import settings

from builder.models import Expansion, Card, PlayerClass, Rarity

def get_data():
	headers = { 'X-Mashape-Key': settings.API_TOKEN }
	response = requests.get(settings.URL, headers=headers)
	return response.json()

def clean_data(data):
	excluded_cardSets = settings.BLACKLIST

	clean_expansions = []
	clean_cards = []
	classes = []
	rarities = []

	for cardSet, cardList in data.items():
		if cardSet in excluded_cardSets:
			continue
		clean_expansions.append(cardSet)
		for card in cardList:
			if card['type'] == 'Hero':
				continue
			if card['playerClass'] not in classes:
				classes.append(card['playerClass'])
			if card['rarity'] not in rarities:
				rarities.append(card['rarity'])	
			clean_card = {
				'expansion': cardSet,
				'card_id': card['cardId'],
				'name': card['name'],
				'player_class': card['playerClass'],
				'rarity': card['rarity'],
				'cost': card['cost'],
				'image': card['img'],
				'image_gold': card['imgGold'],
				'locale': card['locale']
			}
			clean_cards.append(clean_card)
	return clean_expansions, clean_cards, classes, rarities

def create_expansions(data):
	expansion_records = [Expansion(name=name) for name in data]
	Expansion.objects.bulk_create(expansion_records)

def create_cards(data):
	expansions = Expansion.objects.all()
	expansion_map = {e.name:e for e in expansions}

	classes = PlayerClass.objects.all()
	classes_map = {e.name:e for e in classes}

	rarities = Rarity.objects.all()
	rarity_map = {e.name:e for e in rarities}

	for card in data:
		card['expansion'] = expansion_map[card['expansion']]
		card['player_class'] = classes_map[card['player_class']]
		card['rarity'] = rarity_map[card['rarity']]

	card_records = [Card(**card_fields) for card_fields in data]
	Card.objects.bulk_create(card_records)

def create_classes(data):
	classes = [PlayerClass(name=name) for name in data]
	PlayerClass.objects.bulk_create(classes)

def create_rarities(data):
	rarities = [Rarity(name=name) for name in data]
	Rarity.objects.bulk_create(rarities)

def sync():
	data = get_data()
	clean_expansions, clean_cards, classes, rarities = clean_data(data)

	Expansion.objects.all().delete()
	PlayerClass.objects.all().delete()
	Rarity.objects.all().delete()

	create_classes(classes)
	create_rarities(rarities)
	create_expansions(clean_expansions)
	create_cards(clean_cards)

