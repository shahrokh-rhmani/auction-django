from django import template
from django.utils import timezone


register = template.Library()


@register.filter(name="time_left")
def time_left(value):
    t = value - timezone.now()
    days, seconds = t.days, t.seconds
    hours =  seconds // 3600 # 60**2 # 86400 // 3600 = 24
    minutes = (seconds % 3600) // 60 # 12600 % 3600 = 1800 ==> 1800 // 60 = 30
    seconds = seconds % 60 # seconds % (24 * 3600) % 60
    if value > timezone.now():
        return str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"
    else:
        return 0


    


