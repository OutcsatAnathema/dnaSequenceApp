from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def health(request):
    return render(request, 'health.html')

def medicine(request):
    return render(request, 'medicine.html')

def news(request):
    return render(request, 'news.html')

def client(request):
    return render(request, 'client.html')

def contact(request):
    return render(request, 'contact.html')