from django import forms

from .models import Message

class ContactForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = [
			'fullname',
			'email',
			'subject',
			'message',
		]

		labels = {'fullname': 'Full name'}
	
