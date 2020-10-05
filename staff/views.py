from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .models import Staff
from .admin import UserCreationForm, UserChangeForm

# Create your views here.
def index(request):
    logout(request)
    if request.method == 'POST':
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'staff/index.html')

@login_required
def dashboard(request):
    return render(request, 'staff/dashboard.html')

@login_required
def view(request):
    all_staff = Staff.objects.all()
    return render(request, 'staff/view.html', {'all_staff': all_staff})

@login_required
def add(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff:index'))
    return render(request, 'staff/add.html', {'form': form})

@login_required
def update(request, staff_id):
    staff = Staff.objects.get(id=staff_id)
    form = UserChangeForm(instance=staff)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('staff:index'))
    return render(request, 'staff/update.html', {'form': form})

@login_required
def delete(request, staff_id):
    staff = Staff.objects.get(id=staff_id).delete()
    return HttpResponseRedirect(reverse('staff:index'))