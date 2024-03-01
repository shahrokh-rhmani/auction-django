from .models import UserDetails, Auction, Bid
from django.utils import timezone
from datetime import datetime, timedelta


def increase_bid(user, auction):
    """
    Removes €1.0 from user.
    Creates a Bid record
    Increase the auction's number of bids

    Parameters
    ----------
    auction : class 'models.Auction 
    """

    userDetails = UserDetails.objects.get(user_id=user.id)
    userDetails.balance = float(userDetails.balance) - 1.0
    user.save()
    bid = Bid()
    bid.user_id = user
    bid.auction_id = auction
    bid.bid_time = timezone.now()
    bid.save()
    
    auction.number_of_bids += 1
    auction.time_ending = timezone.now() + timedelta(minutes=1)
    auction.save()


def remaining_time(auction):
    time_left = auction.time_ending - timezone.now() 
    expired = time_left.days
    return time_left, expired