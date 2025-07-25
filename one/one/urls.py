from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

admin.site.site_header = "Knowledge Nook Library Portal"
admin.site.site_title = "Knowledge Nook Library Admin Portal"
admin.site.index_title = "Welcome to Knowledge Nook Library Portal"

def redirect_admin_logout(request):
    return redirect('/login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('two.urls')),
    re_path(r'^admin/logout/$', redirect_admin_logout),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
