"""playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from music import views

music_router = routers.DefaultRouter()
music_router.register(r"instruments", views.InstrumentViewSet)
music_router.register(r"musicians", views.MusicianViewSet)
music_router.register(r"genres", views.GenreViewSet)
music_router.register(r"albums", views.AlbumViewSet)
music_router.register(r"tracks", views.TrackViewSet)


urlpatterns = [
    path("music/", include(music_router.urls)),
    path("admin/", admin.site.urls),
]
