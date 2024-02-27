##
from django.shortcuts import  get_object_or_404
from auction.models import Auction
from django.utils import timezone

auction = get_object_or_404(Auction, id=3)     
time_left = auction.time_ending - timezone.now()
print(time_left.days)
print(time_left.seconds) 

##
    <div class="d-flex justify-content-center">
        <div class="p-2">
            <div id="replacement">
                {% include 'products.html' %}
            </div>
        </div>
    </div>