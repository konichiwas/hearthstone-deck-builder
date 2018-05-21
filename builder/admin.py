from django.contrib import admin

from .models import Expansion, Card, PlayerClass, AddNews, PromoExpansion

@admin.register(Expansion)
class ExpansionAdmin(admin.ModelAdmin):
	list_display = ['name', 'status']
	list_editable = ['status']

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
	list_display = ['name', 'expansion', 'player_class', 'rarity', 'cost']
	list_filter = ['expansion', 'player_class', 'rarity']

@admin.register(PlayerClass)
class PlayerClassAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(AddNews)
class AddNewsAdmin(admin.ModelAdmin):
	list_display = ['date']

@admin.register(PromoExpansion)
class PromoExpansionAdmin(admin.ModelAdmin):
	list_display = ['expansion']