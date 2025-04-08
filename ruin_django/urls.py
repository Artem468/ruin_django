"""
URL configuration for ruin_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve

from core import views
from ruin_django.settings import FRONTEND

urlpatterns = [
    path('api/v1/', include('core.urls')),
    path('admin/', admin.site.urls),
    re_path(r'assets/(?P<path>.*)$', serve,
            {
                'document_root': os.path.join(
                    FRONTEND,
                    'assets'
                )
            }),
    re_path(r'^guides/?$', views.front, name='front'),
    re_path(r'^gallery/?$', views.front, name='front'),
    re_path(r'^tour/<int:id>?$', views.front, name='front'),
    re_path(r'', views.front, name='front'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
