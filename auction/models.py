from django.contrib.auth.models import User
from django.db import models

#     UserDetails
class UserDetails(models.Model):
    user_id = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=2)
    cellphone = models.CharField(max_length=14, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=45, blank=True, null=True)
    post_code = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.user_id.username


class Product(models.Model):
    CATEGORIES = (
        ('LAP', 'Laptop'),
        ('CON', 'Console'),
        ('GAD', 'Gadget'),
        ('GAM', 'Game'),
        ('TEL', 'TV')
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES
    )
    date_posted = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "ID:" + str(self.pk) + " "  + self.title
    

class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_or_bids = models.IntegerField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()

    def __str__(self):
        return "ID:" + str(self.pk) + " PRODUCT_ID:" + str(self.product_id)


class Watchlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

    def __str__(self):
        return "USER_ID:" + str(self.user_id) + " AUCTION_ID:" + str(self.auction_id)
    
    

