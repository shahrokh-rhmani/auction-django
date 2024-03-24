from . import views
from django.urls import path


# app_name = "website"

urlpatterns = [
    path('', views.listview, name='list_view'),
    path('bid/<int:auction_id>/', views.detailview, name='detail_view'),
    path('bid/<int:auction_id>/raise_bid/', views.raise_bid, name='raise_bid'),
    path('watchlist/<int:auction_id>/', views.watchlist, name='watchlist'),
    path('watchlist/', views.watchlist_page, name='watchlist'),
]