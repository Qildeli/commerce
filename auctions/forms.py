from django import forms
from .models import Auction


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description', 'start_price', 'image_url', 'category']


class BidForm(forms.Form):
    amount = forms.DecimalField(label='Your Bid', decimal_places=2)