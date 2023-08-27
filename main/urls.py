from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.index,name='index'),
    path('url-click-counter/', views.urlclick,name='urlclick'),
    path('contact/', views.contact,name='contact'),
    path('privacy-policy/', views.privacy,name='privacy'),
    path('report-malicious-url/', views.reportmal,name='reportmal'),
    path('terms-of-service/', views.termsof,name='termsof'),
    
    path('shorten_url/', views.shorten_url, name='shorten_url'),
    path('<str:short_key>/', views.redirect_to_long_url, name='redirect_to_long_url'),

]