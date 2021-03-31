from django.contrib import admin
from django.urls import path
from .viwes import change, translate, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', change),
    path('translate', translate),
    path('login', login),
]
