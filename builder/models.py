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

class New(models.Model):
	date = models.DateField(auto_now_add=True)
	content = models.TextField()

	def __str__(self):
		return '%s %s' % (self.date, self.content)

class Promo(models.Model):
	expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/', default='')
	order = models.PositiveIntegerField(default=1)

	class Meta:
		ordering = ['-order']
		
	def __str__(self):
		return self.expansion.name

class Message(models.Model):
	fullname = models.CharField(max_length=250)
	email = models.EmailField()
	subject = models.CharField(max_length=250)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return self.message

