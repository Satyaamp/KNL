from django.contrib import admin
from django.urls import path
from two import views
from . import views
from .views import registration_view

from django.contrib.auth.views import LogoutView
from .views import custom_logout

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
   path('profile/', views.profile, name='profile'),
   path('logout/', custom_logout, name='logout'),
   # path('logout-redirect/', views.logout_redirect, name='logout_redirect'),
]






