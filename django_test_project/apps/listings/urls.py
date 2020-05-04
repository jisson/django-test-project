from django.urls import path

from . import views

app_name = "listings"
urlpatterns = [
    path("", views.ListingViewSet.as_view(), name="listings",),
    path("active/", views.ActiveListingViewSet.as_view(), name="active_listings",),
]
