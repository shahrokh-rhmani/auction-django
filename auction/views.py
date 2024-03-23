from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone
from datetime import datetime
from itertools import chain

from .models import Auction, UserInfo, Watchlist, Bid
from .transactions import increase_bid, remaining_time
from django.urls import reverse
from django.http import HttpResponseRedirect


def listview(request):
    auctions = Auction.objects.all()
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)


        w = Watchlist.objects.filter(user_id=user)
        watchlist = Auction.objects.none()
        for item in w:
            a = Auction.objects.filter(id=item.auction.id)
            watchlist = list(chain(watchlist, a))
                
        return render(request, 'listview.html', {
            'auctions': auctions, 'watchlist': watchlist})
    else:
        return render(request, 'listview.html', {'auctions': auctions})
    
    
def detailview(request, auction_id):
    if request.user.is_authenticated:
        auction = get_object_or_404(Auction, id=auction_id)
        if auction.time_starting > timezone.now():
            return redirect('index')
        user = User.objects.get(username=request.user.username)
        stats = []
        time_left, expired = remaining_time(auction)

        stats.append(time_left) # index 0

        if expired < 0: # index 1
            stats.append(True)
            auction.expired = True
            auction.save()
        else:
            stats.append(False)

        
        current_cost = auction.base_price + (auction.number_of_bids * 20)
        current_cost = "%0.2f" % current_cost
        stats.append(current_cost) # index 2

    
    
        latest_bid = Bid.objects.all().order_by('-bid_time') # index 3
        if latest_bid:
            winner = User.objects.get(id=latest_bid[0].user.id)
            stats.append(winner.username)
            auction.final_price = current_cost
            auction.save()

        else:
            
            stats.append(None)   

       

        #  watchlist
        w = Watchlist.objects.filter(user=user)
        watchlist = Auction.objects.none()
        for item in w:
            a = Auction.objects.filter(id=item.auction.id)
            watchlist = list(chain(watchlist, a))

        return render(request, 'detailview.html', 
            {
                'auction': auction,
                'user': user,
                'stats': stats,
                'watchlist': watchlist,
                'latest_bid': latest_bid,
                              
        })
    
    else:
        return redirect('index')

    

def raise_bid(request, auction_id):
    if request.user.is_authenticated:
        auction = Auction.objects.get(id=auction_id) 
        user = User.objects.get(username=request.user.username)
        
        latest_bid = Bid.objects.filter(auction=auction.id).order_by('-bid_time')
        if not latest_bid:    
            increase_bid(user, auction)
        else:
            current_winner = User.objects.filter(id=latest_bid[0].user.id)

            if current_winner[0].id != user.id:
                increase_bid(user, auction)
        return redirect('bid_page', auction_id)
    else:
        return redirect('index')


    
def watchlist(request, auction_id): # watch or unwatch button
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            auction = Auction.objects.get(id=auction_id)
            w = Watchlist.objects.filter(auction_id=auction_id)
            if not w:
                watchlist_item = Watchlist()
                watchlist_item.auction = auction
                watchlist_item.user = user
                watchlist_item.save()
            else:
                w.delete()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return redirect('login') 
               
            

def watchlist_page(request): 
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        w = Watchlist.objects.filter(user_id=user)

        auctions = Auction.objects.none()
        for item in w:
            a = Auction.objects.filter(id=item.auction.id, time_ending__gte=timezone.now())
            auctions = list(chain(auctions, a))
        return render(request, 'listview.html', {
            'auctions': auctions,
            'user': user,
            'watchlist': auctions
        })

    else:
        return redirect('login')

    