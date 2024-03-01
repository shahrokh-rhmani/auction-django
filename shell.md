## 
from django.utils import timezone
from auction.models import Auction

print(timezone.now())
t = Auction.time_starting
print(t)

a = Auction.objects.all().first()
print(a.time_starting)
for item in a :
    print(item)

[x for x in Auction().__dict__.keys() if not x.startswith('_')]
