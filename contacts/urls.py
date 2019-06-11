"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from core.views import people_view, new_person, modify, delete, show

urlpatterns = [
    path('', people_view, name='list'),
    path('new', new_person, name='new'),
    re_path(r'^delete/(?P<id>[0-9]+)/$', delete),
    re_path(r'^modify/(?P<id>[0-9]+)/$', modify),
    re_path(r'^show/(?P<id>[0-9]+)/$', show)
]
# 1. Tworzenie formularza do stworzenia nowego modelu dla osoby (/new).2.
# Tworzenie nowej osoby (formularz wysyłany POST-em na adres /new).
# 3. Tworzenie formularza do modyfikacji osoby (/modify/{id}).
# 4. Modyfikacja osoby (formularz wysyłany POST-em na adres /modify/{id}).
# 5. Usunięcie podanej osoby (/delete/{id}).
# 6. Pokazanie jednej osoby (/show/{id}).
