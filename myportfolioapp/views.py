import os

from django.contrib import messages
from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import *
# Create your views here.

def home(request):
    context={
        'about':About.objects.all(),
        'services': service.objects.all(),
        'skills': skill.objects.all(),
        'exps': experience.objects.all(),
        'teams': team.objects.all(),
    }
    return render(request,'index.html',context)


#send message
def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            return redirect('success')
    else:
        form = ContactForm()
        return render(request,'contact/contact.html',{'form':form})

class ContactSuccessView(TemplateView):
    template_name = 'contact/success.html'

def LeaveMessage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        leavemsg=LeftMessage()
        leavemsg.name=name
        leavemsg.email=email
        leavemsg.subject=subject
        leavemsg.message=message
        leavemsg.save()
        messages.success(request,'Your message has been received!')
        return redirect('home')

def downloadcv(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as f:
            response=HttpResponse(f.read(),content_type="application/cv")
            response['Content-Dispotion']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404
