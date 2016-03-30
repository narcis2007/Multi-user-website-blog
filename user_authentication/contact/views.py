from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth import get_user
from models import ContactMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
from contact.forms import ContactForm


def addContactMessage(request):
    if request.POST:
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'Thanks for contacting us!')
            return HttpResponseRedirect('/')

    form=ContactForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render(request,'contact/contact.html',args)

'''
    trebuie sa verific si de permisiune(superuser) la contacts!!!!
    FOARTE IMPORTANT!
'''
@login_required
def all_contacts(request):
    args={}
    args.update(csrf(request))
    args['contacts']=ContactMessage.objects.all()[::-1]
    return render(request,'contact/contact_messages.html',args)
