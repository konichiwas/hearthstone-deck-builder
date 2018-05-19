from django import forms

from .models import Card, Expansion

class SearchForm(forms.ModelForm):
	class Meta:
		model = Card
		fields = [
			'expansion', 'player_class', 'rarity',
		]
		
	COST_CHOICES = [
		(None, '----------'),
		('0', '0'),
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4'),
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8+'),
	]

	FORMAT_CHOICES = Expansion.STATUS_CHOICES

	cost = forms.ChoiceField(choices=COST_CHOICES, required=False)
	FORMAT = forms.ChoiceField(choices=FORMAT_CHOICES, required=False)

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['expansion'].required=False
		self.fields['player_class'].required=False
		self.fields['rarity'].required=False

	def get_data(self):
		params = {}
		query = {}
		data = self.cleaned_data
		
		for k in data:
			if data[k]:
				if k is 'cost':
					params[k] = data[k]
					if int(data[k]) < 8:
						query['cost'] = int(data['cost'])
					else:
						query['cost__gte'] = int(data['cost'])
				elif k is 'FORMAT':
					params[k] = data[k]
					if data[k] < 'wild':
						query['expansion__status'] = data[k]		 
				else:
					params[k] = data[k].id
					query[k] = data[k]		

		cards = Card.objects.filter(**query).order_by('cost')
		return cards, params