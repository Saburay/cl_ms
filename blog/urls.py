from django.contrib import admin
from django.urls import path

from blog import views

urlpatterns = [
    path("", views.ShowNewsView.as_view(), name='blog-home'),
    path("news/<int:pk>/", views.NewsDetailView.as_view(), name='news-detail'),
    path("news/add/", views.CreateNewsView.as_view(), name='news-add'),
    path("news/<int:pk>/update/", views.UpdateNewsView.as_view(), name='news-update'),
    path("news/<int:pk>/delete/", views.DeleteNewsView.as_view(), name='news-delete'),
    path("contacts/", views.contacts, name='blog-contacts'),
]
