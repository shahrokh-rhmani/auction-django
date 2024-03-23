from django.contrib.auth.models import User
from django.db import models



class UserDetails(models.Model):
    user = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    cellphone = models.CharField(max_length=14, blank=True, null=True)
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
    number_of_bids = models.IntegerField()
    base_price = models.FloatField(null=True)
    final_price = models.FloatField(null=True)
    expired = models.BooleanField(default=False)
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField(null=True, blank=True)

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
    


    

