from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField

class Article(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	image = ThumbnailerImageField(upload_to='news-images/')
	title = models.CharField(max_length=1000)
	content = RichTextUploadingField()

	class Meta:
		ordering = ['-date']
		
	def __str__(self):
		return '%s %s' % (self.date, self.title)

	def get_absolute_url(self):
		return reverse('news:new', kwargs={'id': self.id})