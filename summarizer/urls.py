from django.urls import path
from summarizer import views

urlpatterns = [
    path("", views.home, name="home"),
]