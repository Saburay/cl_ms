from django.shortcuts import render
from .models import News

news = [
    {
        'title': 'Our first publication',
        'text': 'some text',
        'date': '2023',
        'author': 'some author'
    },
{
        'title': 'Our second publication',
        'text': 'some 2th text',
        'date': '2023',
        #'author': 'some another author'
    }
]

def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Blog home page'

    }
    return render(request, 'blog/home.html', data)

def contacts(request):
    return render(request, 'blog/contacts.html', {'title':'Contacts page'})