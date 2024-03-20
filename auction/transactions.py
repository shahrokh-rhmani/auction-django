from .models import UserDetails, Bid
from django.utils import timezone
from datetime import timedelta


def increase_bid(user, auction):
    userDetails = UserDetails.objects.get(user=user.id)
    userDetails.balance = float(userDetails.balance) - 1.0
    user.save()
    
    bid = Bid()
    bid.user = user
    bid.auction = auction
    bid.bid_time = timezone.now()
    bid.save()
    
    auction.number_of_bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=1)
    auction.save()


def remaining_time(auction):
    time_left = auction.time_ending - timezone.now() 
    days, seconds = time_left.days, time_left.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_left = str(minutes) + "m " + str(seconds) + "s"
    expired = days
    return time_left, expired