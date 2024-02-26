from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='search')
def search(value, id):
    """
    Linear search of a list

    Parameters
    ----------
    value : list
        A list with key values
    id : int
        The key we are searching
    
    Returns
    ------
    boolean
        True if the key is found, False otherwise.
    """
    for v in value:
        if v.id == id:
            return True
    
    return False

@register.filter(name="time_left")
def time_left(value):
    t = value - timezone.now()
    return t

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