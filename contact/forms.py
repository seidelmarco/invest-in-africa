from .models import Message
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'phone', 'message_text')




