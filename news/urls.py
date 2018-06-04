from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
	path('articles/', views.get_articles, name='news'),
	path('articles/<id>/', views.get_article, name='new'),
]