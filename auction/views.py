from django.contrib.auth.models import User
from django.shortcuts import render
from datetime import datetime
from itertools import chain

from .models import Auction, UserDetails, Watchlist


def index(request):
    """
    The main page of the website

    Returns
    ------
    HTTPResponse
        The index page with the current and future auctions.
    """
    auctions = Auction.objects.filter(time_ending__gte=datetime.now()).order_by('time_starting')

    try:
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)

            w = Watchlist.objects.filter(user_id=user)
            watchlist = Auction.objects.none()
            for item in w:
                a = Auction.objects.filter(id=item.auction_id.id)
                watchlist = list(chain(watchlist, a))
            
            userDetails = UserDetails.objects.get(user_id=user.id)
            return render(request, 'index.html', 
                          {'auctions': auctions, 'balance': userDetails.balance, 'watchlist': watchlist})
    except KeyError:
        return render(request, 'index.html', {'auctions': auctions})
    
    return render(request, 'index.html', {'auctions': auctions})


def filter_auctions(request, category):
    pass