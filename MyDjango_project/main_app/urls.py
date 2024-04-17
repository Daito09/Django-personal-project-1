from django.urls import path
from .views import home_page, class_page, blog_page, about_page




urlpatterns=[
    path("", home_page, name="home"),
    path("", class_page, name="class"),
    path("", blog_page, name="blog"),
    path("", about_page, name="about"),
]