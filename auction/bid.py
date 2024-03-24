from .models import  Bid
from django.utils import timezone
from datetime import timedelta


def bid_increment(user, auction):
    bid = Bid()
    bid.user = user
    bid.auction = auction
    bid.bid_time = timezone.now()
    bid.save()
    
    auction.count_bids += 1
    auction.time_end = timezone.now() + timedelta(minutes=1)
    auction.save()


def time_left_detail(auction):
    time_left = auction.time_end - timezone.now() 
    days, seconds = time_left.days, time_left.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    time_left = str(minutes) + "m " + str(seconds) + "s"
    expired = days
    return time_left, expired