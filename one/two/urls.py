from django.contrib import admin
from django.urls import path
from two import views
from . import views
from .views import registration_view, confirmation_view

urlpatterns = [
   path("", views.index, name='two'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("terms", views.terms, name='terms'),
   path("privacy", views.privacy, name='privacy'),
   path("faq", views.faq, name='faq'),
   path("feedback", views.feedback, name='feedbak'),
   path("complaint", views.complaint, name='complaint'),
   path("suggestion", views.suggestion, name='suggestion'),
   path("book", views.book, name='book'),
   path("sitemap", views.sitemap, name='sitemap'),
   path("login", views.login, name='login'),
    path('registration', registration_view, name='registration'),
    path('confirmation/', confirmation_view, name='confirmation'),
  
]






