from django import forms
from .models import Products, Stores

# Form
class StoreForm(forms.Form):

    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    contact_no = forms.CharField(max_length=12)
    landmark = forms.CharField(max_length=200)
    email = forms.EmailField()
    location = forms.CharField(max_length=50)


#Model Form
class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = '__all__'
        #exclude = ('ratings', )

