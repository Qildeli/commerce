from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
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
    category = models.ForeignKey('Category', related_name="listings", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


def validate_non_negative(value):
    if value < 0:
        raise ValidationError('Amount must be a non-negative value.')


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_non_negative])
    date_placed = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="bids_placed", on_delete=models.CASCADE) # Relation to User Model, indicating the user who placed the bid
    listing = models.ForeignKey(Auction, related_name="bids_on_item", on_delete=models.CASCADE) # Relation to Auction Listing Model

    def __str__(self):
        return f"{self.user.username} bid {self.amount} on {self.listing.title}"


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posted_comment", on_delete=models.CASCADE) # Relation to User Model, indicating the user who posted the comment
    listing = models.ForeignKey(Auction, related_name="comments", on_delete=models.CASCADE) # Relation to Auction Listing Model

    def __str__(self):
        return f"Comment by {self.user.username} on {self.listing.title}"


class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="watchlist_items", on_delete=models.CASCADE)
    listing = models.ForeignKey(Auction, related_name="watched_by", on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
