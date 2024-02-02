from django.contrib import admin
from .models import Auction, UserDetails, Product, Watchlist




admin.site.register(UserDetails)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Watchlist)