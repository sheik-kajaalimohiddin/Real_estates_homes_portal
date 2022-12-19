from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelformset_factory
from django.views.generic import ListView
from .forms import CreateListForm
#ImageForm

import users.models
from .models import *
from users.models import *


# Create your views here.
def homefeaturedProperty(request):
    profile = Profile.objects.all()
    listing = Listing.objects.filter(featuredProperty='True')
    context = {'listing': listing,'profile': profile}
    return render(request,'realtor/home.html',context)

class aboutListView(ListView):
    model = Profile
    template_name = 'realtor/about.html'

def listings(request):
    listing = Listing.objects.all()
    context = {'listing':listing}
    return render(request,'realtor/listings.html',context)

def realtorlistings(request):
    listing = Listing.objects.all()
    context = {'listing':listing}
    return render(request,'realtor/realtorListings.html',context)

def createListing(request):
    if request.method == "POST":
        prod = Listing()
        prod.propertyName = request.POST.get('Name')
        prod.propertyDescription = request.POST.get('Description')
        prod.propertyAddress = request.POST.get('Address')
        prod.propertyType = request.POST.get('type')
        prod.propertyNeighborhood = request.POST.get('Neighborhood')
        prod.propertyZipCode = request.POST.get('ZipCode')
        prod.propertyPrice = request.POST.get('Price')
        prod.propertyStatus = request.POST.get('Status')
        value = request.POST.get('featured')
        if value == 'on':
            value = True
        else:
            value = False
        prod.featuredProperty = value
        if len(request.FILES) != 0:
            prod.propertyImage1 = request.FILES['propertyImage1']
            prod.propertyImage2 = request.FILES['propertyImage2']
            prod.propertyImage3 = request.FILES['propertyImage3']
            prod.propertyImage4 = request.FILES['propertyImage4']
        prod.save()
        messages.success(request, "Listing added successfully")
        return redirect("/")
    return render(request, 'realtor/createListing.html')
def events(request):
    return render(request,'realtor/events.html',{'title':'events'})

def login(request):
    return render(request,'realtor/login.html',{'title':'login'})


def search(request):
    return render(request,'realtor/search.html',{'title':'search'})
def detailedView(request, pk):
    property = Listing.objects.get(id=pk)
    context = {'item': property, }
    return render(request, 'realtor/detailedView.html', context)

def updateProperty(request, pk):

    item = Listing.objects.all()
    property = Listing.objects.get(id=pk)
    form = CreateListForm(instance=property)
    if request.method == 'POST':
        form = CreateListForm(request.POST, request.FILES,instance=property)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form, 'item':property}
    return render(request, 'realtor/property_form.html', context)

def deleteProperty(request, pk):
    property = Listing.objects.get(id=pk)
    if request.method == 'POST':
        property.delete()
        return redirect('/realtorlistings/')
    context = {'item':property}
    return render(request, 'realtor/delete_property.html', context)

def requestForm(request):
    return render(request, 'realtor/Request_Form.html')

def requestSubmitForm(request):
    return render(request, 'realtor/Request_Submited_Success.html')


class PropertyTypeSearchView(ListView):
    model = Listing
    template_name='realtor/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('type')
        return Listing.objects.filter(propertyType=query)

class PropertyNeighborhoodSearchView(ListView):
    model = Listing
    template_name='realtor/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('neighborhood')
        return Listing.objects.filter(propertyNeighborhood=query)

class PropertyZipCodeSearchView(ListView):
    model = Listing
    template_name='realtor/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('zipcode')
        return Listing.objects.filter(propertyZipCode=query)

class PropertyPriceSearchView(ListView):
    model = Listing
    template_name = 'realtor/search.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('price')
        return Listing.objects.filter(propertyPrice=query)