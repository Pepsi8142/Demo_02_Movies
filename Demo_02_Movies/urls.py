"""
URL configuration for Demo_02_Movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, UnknownViewSet, ComedyViewSet
from django.conf.urls.static import static
from django.conf import settings

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'movies', MovieViewSet, basename='movies')
router.register(r'action', ActionViewSet, basename='action')
router.register(r'unknown', UnknownViewSet, basename="unknown")
router.register(r'comedy', ComedyViewSet, basename='comedy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)