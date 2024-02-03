from . import views
from django.urls import path


# app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('bid/<int:auction_id>/', views.bid_page, name='bid_page'),
    path('bid/<int:auction_id>/raise_bid/', views.raise_bid, name='raise_bid'),
]