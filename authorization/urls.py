from django.contrib import admin
from django.urls import path

from .views import login_page, login, logout

app_name = 'login'

urlpatterns = [
    path('', login_page, name='login_page'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
