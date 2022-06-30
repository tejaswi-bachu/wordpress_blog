from django.urls import path

from . import views
urlpatterns = [
    path('', views.NotyMessageView.as_view())
]