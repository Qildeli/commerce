from django.contrib.auth.models import AbstractUser
from django.db import models
from commerce import settings

class User(AbstractUser):
    pass

class Auction(models.Model):
    # Define choices for the 'status' field
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Ended', 'Ended'),
        ('Cancelled', 'Cancelled')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(upload_to='auction_images/', blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="auctions_owned", on_delete=models.CASCADE) #Relation to User Model, indicating the user who posted the listing
    winner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="auctions_won", null=True, on_delete=models.SET_NULL) # Relation to User Model, indicating the user who won the auction; default is null until the auction ends

    def __str__(self):
        return self.title


class Bid(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.DecimalField(min_value=0)
    date_placed = models.DateTimeField()
    user_id = models.ForeignKey() # Relation to User Model, indicating the user who placed the bid
    listing_id = models.ForeignKey() # Relation to Auction Listing Model

class Comment():
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    date_posted = models.DateTimeField()
    user_id = models.ForeignKey() # Relation to User Model, indicating the user who posted the comment
    listing_id = models.ForeignKey() # Relation to Auction Listing Model

class Watchlist():
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey() # Relation to User Model
    listing_id = models.ForeignKey() # Relation to Auction Listing Model