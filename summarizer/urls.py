from django.urls import path
from summarizer import views

urlpatterns = [
    #path("", views.home, name="home"),
    path("video/", views.video_view, name="summarize-video"),
    path("article/", views.article_view, name="summarize-article"),
    path("image/", views.image_view, name="summarize-image"),
    path("pdf/", views.pdf_view, name="summarize-pdf"),
]