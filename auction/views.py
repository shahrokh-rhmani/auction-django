from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone
from itertools import chain

from .models import Auction, Watchlist, Bid
from .bid import bid_increment, time_left_detail
from django.http import HttpResponseRedirect


def listview(request):
    auctions = Auction.objects.all()
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)


        w = Watchlist.objects.filter(user=user)
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
        if auction.time_start > timezone.now():
            return redirect('list_view')
        user = User.objects.get(username=request.user.username)
        stats = []
        time_left, expired = time_left_detail(auction)

        stats.append(time_left) # index 0

        if expired < 0: 
            stats.append(True) # index 1
            auction.expired = True
            auction.save()
        else:
            stats.append(False) # index 1

        
        current_cost = auction.base_price + (auction.count_bids * 20)
        current_cost = "%0.2f" % current_cost
        stats.append(current_cost) # index 2

    
    
        latest_bid = Bid.objects.all().order_by('-bid_time') 
        if latest_bid:
            winner = User.objects.get(id=latest_bid[0].user.id)
            stats.append(winner.username) # index 3
            auction.final_price = current_cost
            auction.save()

        else:
            
            stats.append(None) # index 3

       

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
        return redirect('list_view')

    

def bid(request, auction_id):
    if request.user.is_authenticated:
        auction = Auction.objects.get(id=auction_id) 
        user = User.objects.get(username=request.user.username)
        
        latest_bid = Bid.objects.filter(auction=auction.id).order_by('-bid_time')
        if not latest_bid:    
            bid_increment(user, auction)
        else:
            current_winner = User.objects.filter(id=latest_bid[0].user.id)

            if current_winner[0].id != user.id:
                bid_increment(user, auction)
        return redirect('detail_view', auction_id)
    else:
        return redirect('list_view')


    
def watchlist(request, auction_id): # watch or unwatch button
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            auction = Auction.objects.get(id=auction_id)
            w = Watchlist.objects.filter(auction=auction)
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
               
            

def watchlistview(request): 
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        w = Watchlist.objects.filter(user=user)

        auctions = Auction.objects.none()
        for item in w:
            a = Auction.objects.filter(id=item.auction.id, time_end__gte=timezone.now())
            auctions = list(chain(auctions, a))
        return render(request, 'listview.html', {
            'auctions': auctions,
            'user': user,
            'watchlist': auctions
        })

    else:
        return redirect('login')

    