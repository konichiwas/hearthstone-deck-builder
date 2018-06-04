from django.contrib import admin

from .models import Expansion, Card, PlayerClass, Promo, Message

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

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
	list_display = ['expansion']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ['fullname','subject', 'email', 'date']
	list_filter = ['email', 'date']