from django import forms

from .models import Message

class ContactForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = [
			'name',
			'lastname',
			'email',
			'message',
		]
		widgets = {
			'message': forms.Textarea
		}		
