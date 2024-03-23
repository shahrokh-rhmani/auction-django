from django.contrib import admin
from .models import Auction, UserInfo, Product, Watchlist, Bid




admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Watchlist)
admin.site.register(Bid)