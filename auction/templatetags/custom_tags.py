from django import template
from django.utils import timezone


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


    


