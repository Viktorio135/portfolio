from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from .forms import UserLoginForm

def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index_page"))
                # return render(request, 'index.html')
    else:
        form = UserLoginForm()
    
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index_page"))