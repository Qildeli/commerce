from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Auction
from .forms import CreateListingForm


def index(request):
    # Query for active listings
    listings = Auction.objects.filter(status="Active")

    # Pass the listings to the template
    context = {
        'listings': listings
    }

    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        form = CreateListingForm(request.POST, request.FILES)  # Note: request.FILES is needed if you're uploading files
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.owner = request.user  # set the owner to the currently logged-in user
            new_listing.current_price = new_listing.start_price  # set the current price to the starting price
            new_listing.save()
            return HttpResponseRedirect(reverse("index"))  # Redirect to homepage or to the new listing's page after creation
    else:
        form = CreateListingForm()

    return render(request, "auctions/create_listing.html", {
        "form": form
    })


def listing_page(request, listing_id):
    listing = get_object_or_404(Auction, id=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'auctions/listing_page.html', context)


def toggle_watchlist(request, auction_id):
    auction = get_object_or_404(Auction, id=auction_id)
    if request.user in auction.watchlist_users.all():
        auction.watchlist_users.remove(request.user)
    else:
        auction.watchlist_users.add(request.user)
    auction.save()
    return redirect('listing_page', listing_id=auction.id)
