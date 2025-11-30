from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('gallery/', views.gallery, name='gallery'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('product/', views.product, name='product'),
    path('notfound/', views.notfound, name='notfound'),
]
