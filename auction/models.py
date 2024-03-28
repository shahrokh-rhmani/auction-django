from django.contrib.auth.models import User
from django.db import models



class UserInfo(models.Model):
    user = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count_bids = models.IntegerField()
    base_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    price_per_bid = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    final_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    expired = models.BooleanField(default=False)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.auction}"
    

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user} | {self.auction}"
    


    

