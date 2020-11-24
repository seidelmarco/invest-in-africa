from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        contact_form.save()
        #complete_message = request.POST['name', 'email', 'phone', 'message_text', ]
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message_text = request.POST['message_text']
        return render(request, 'contact/index.html', {'name': name,
                                                      'email': email,
                                                      'phone': phone,
                                                      'message_text': message_text,
                                                      #'complete_message': complete_message,
                                                      })

    else:
        return render(request, 'contact/index.html', {})


