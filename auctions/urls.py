from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create_listing"),
    path('listing/<int:listing_id>/', views.listing_page, name='listing_page'),
    path('toggle_watchlist/<int:auction_id>/', views.toggle_watchlist, name='toggle_watchlist'),
    path('close_auction/<int:listing_id>/', views.close_auction, name='close_auction'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('categories/', views.all_categories, name='all_categories'),
    path('category/<int:category_id>/', views.category_listings, name='category_listings')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

