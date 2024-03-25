from . import views
from django.urls import path


# app_name = "website"

urlpatterns = [
    path('', views.listview, name='list_view'),
    path('bid/<int:auction_id>/', views.detailview, name='detail_view'),
    path('bid/<int:auction_id>/bid_increment/', views.bid, name='bid'),
    path('watchlist/<int:auction_id>/', views.watchlist, name='watchlist'),
    path('watchlist/', views.watchlistview, name='watchlist'),
]