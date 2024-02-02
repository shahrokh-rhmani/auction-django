from django.contrib import admin
from .models import Auction, UserDetails, Watchlist


admin.site.register(UserDetails)
admin.site.register(Auction)
admin.site.register(Watchlist)