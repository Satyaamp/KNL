from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Knowledge Nook Library Portal"
admin.site.site_title = "Knowledge Nook Library Admin Portal"
admin.site.index_title = "Welcome to Knowledge Nook Library Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('two.urls')),
]
