from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        form=UserCreationForm()
    return render (request,'registration/signup.html',{'form':form})

# Create your views here.
