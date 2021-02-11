from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Clss

# Create your views here.

@login_required
def index(request):
    classes = Clss.objects.all()
    return render(request, 'class/index.html', {'classes': classes})

@login_required
def add(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            fee = request.POST['fee']

            # check if name or fee is empty
            if name is "" or fee is "":
                raise Exception ("Cannot be empty")
            clss = Clss(name=name, fee=fee)
            clss.save()
            return HttpResponseRedirect(reverse('class:index'))
        return render(request, 'class/add.html')
    except Exception as e:
        messages.add_message(request, messages.ERROR, e)
        return render(request, 'class/add.html')

@login_required
def update(request, class_id):
    clss = Clss.objects.get(id=class_id)
    
    if request.method == 'POST':
        # data from form
        name = request.POST['name']
        fee = request.POST['fee']
        # update datbase
        clss.name = name
        clss.fee = fee
        clss.save()
        return HttpResponseRedirect(reverse('class:index'))
    return render(request, 'class/update.html', {'class': clss})

@login_required
def delete(request, class_id):
    clss = Clss.objects.get(id=class_id).delete()
    return HttpResponseRedirect(reverse('class:index'))