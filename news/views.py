from django.shortcuts import render, get_object_or_404

from news.models import Article

def get_articles(request):
	news = Article.objects.all()
	context = {'news': news}
	return render(request, 'news/archive.html', context)

def get_article(request, id):
	new = get_object_or_404(Article, id=id)
	context = {'new': new}
	return render(request, 'news/full-article.html', context)
	
