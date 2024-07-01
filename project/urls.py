from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('portfolio/', portfolio, name="portfolio"),
    path('portfolio/<int:portfolio_id>/', portfolio_detail, name="portfolio-detail"),
    path('contact/', contact, name="contact"),
    path('services/<int:service_id>/', service_detail, name="service-detail"),
    path('ru/blog/<int:pk>/', blog_detail, name="blog-detail"),
]
