from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.homefeaturedProperty, name='realtor-home'),
   #path('', views.homeListView.as_view(), name='realtor-home'),
    path('about/', views.aboutListView.as_view(), name='realtor-about'),
    path('listings/', views.listings, name='listings'),
    path('realtorlistings/', views.realtorlistings, name='realtor-listings'),
    path('events/', views.events, name='realtor-events'),
    path('search/', views.search, name='realtor-search'),
    path('createListing/', views.createListing, name='realtor-createListing'),
   # path('create_property/', views.createProperty, name='realtor-create_property'),
    path('update_property/<str:pk>/', views.updateProperty, name='realtor-update-property'),
    path('delete_property/<str:pk>/', views.deleteProperty, name='realtor-delete-property'),
    path('Request_Form/', views.requestForm, name='realtor-request-information'),
    path('Request_Submited_Success/', views.requestSubmitForm, name='customer-request-submission'),
    path('search_type_listings/', views.PropertyTypeSearchView.as_view(), name='search-type-listings'),
    path('search_neighborhood_listings/', views.PropertyNeighborhoodSearchView.as_view(), name='search-neighborhood-listings'),
    path('search_zipcode_listings/', views.PropertyZipCodeSearchView.as_view(), name='search-zipcode-listings'),
    path('search_price_listings/', views.PropertyPriceSearchView.as_view(), name='search-price-listings'),
    path('detailed_view/<str:pk>/', views.detailedView, name='realtor-detailed-view'),
]
