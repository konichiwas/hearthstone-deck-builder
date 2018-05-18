from django.db import models

class Expansion(models.Model):
	STATUS_CHOICES = [
		('wild','Wild'),
		('standard', 'Standard'),
	]

	name = models.CharField(max_length=250)
	status = models.CharField(
		max_length=250,
		choices=STATUS_CHOICES,
		blank=True
	)

	def __str__(self):
		return self.name

class PlayerClass(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Rarity(models.Model):
	name = models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Card(models.Model):
	expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE)
	card_id = models.CharField(max_length=50)
	name = models.CharField(max_length=100)
	player_class = models.ForeignKey(PlayerClass, on_delete=models.CASCADE)
	rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
	cost = models.PositiveIntegerField(default=0)
	image = models.CharField(max_length=250)
	image_gold = models.CharField(max_length=250)
	locale = models.CharField(max_length=50)

	def __str__(self):
		return self.card_id
