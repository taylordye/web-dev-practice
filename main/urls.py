from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('barry/', views.barry_home, name='barry_home'),
    path('api/signups/', views.fetch_signups, name='fetch_signups'),
    path('listings/', views.listings_home, name='listings_home'),
    path('listings/listing-detail/<int:pk>/', views.listing_detail, name='listing_detail'),
]