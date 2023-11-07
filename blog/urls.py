from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path("", views.ShowNewsView.as_view(), name='blog-home'),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name='news-detail'),
    path("contacts/", views.contacts, name='blog-contacts'),
]
