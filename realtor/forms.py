from django.forms import ModelForm
from django import forms
from django.forms import TextInput
from .models import Listing
#Images

class CreateListForm(ModelForm):
    class Meta:
        model = Listing
#        fields = '__all__'
        fields = ['propertyName', 'propertyDescription', 'propertyNeighborhood', 'propertyZipCode', 'propertyPrice', 'featuredProperty', 'propertyImage1','propertyImage2', 'propertyImage3', 'propertyImage4', ]
#class ImageForm(ModelForm):
#    image = forms.ImageField(label='Image')
#    class Meta:
#        model = Images
#        fields = ['image', ]

