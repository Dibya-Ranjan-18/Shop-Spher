from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('user_auth/', include('user_auth.urls')),
    re_path(r'^images/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]