from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),

]