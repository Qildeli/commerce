from django.contrib import admin
from .models import Auction, Category, Comment, Bid, Watchlist

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Watchlist)

@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'category',)
    search_fields = ('title', 'description')


