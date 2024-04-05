from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index.html'),
    path('health.html', views.health, name='health.html'),
    path('medicine.html', views.medicine, name='medicine.html'),
    path('news.html', views.news, name='news.html'),
    path('contact.html', views.contact, name='contact.html'),
    path('client.html', views.client, name='client.html')
    # Add more URLs as needed
]