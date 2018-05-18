from django.core.management.base import BaseCommand

from sync.client import sync

class Command(BaseCommand):
	def handle(self, *args, **options):
		sync()