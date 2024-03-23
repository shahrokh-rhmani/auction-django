from django import template
from datetime import timedelta
from django.utils import timezone
from ..models import Bid, Auction

register = template.Library()


@register.filter(name="time_left")
def time_left(value):
    t = value - timezone.now()
    days, seconds = t.days, t.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if value > timezone.now():
        return str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"
    else:
        return 0


    


@register.filter(name="current_price")
def current_price(value):
    """
    Calculates the current value
    of the item depending the
    number of bids.

    Parameters
    ----------
    value : IntegerField
        Number of Bids.
    
    Returns
    ------
    string
        Current value with two decimals.
    """
    current_cost = 0.20 + (value.number_of_bids * 0.20)
    current_cost = "%0.2f" % current_cost
    return current_cost