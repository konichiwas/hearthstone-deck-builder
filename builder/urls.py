from django.urls import path

from . import views

app_name = 'builder'

urlpatterns = [
	path('', views.index, name='index'),
	path('album/', views.album, name='album'),
	path('contact/', views.contact, name='contact'),
]