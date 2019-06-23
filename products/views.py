#builtin imports
import os

# third-party imports
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.urls import reverse
from django.views.decorators.cache import cache_page

# project-level imports
from .models import Stores, Products
from .forms import StoreForm, ProductsForm


def home_view(request):
    return render(request, "base.html")


def add_store_details(request):

    with open(r'C:\Users\User\workspace\stores.txt') as std:
        store_data = std.readlines()
        for sd in store_data[1:]:
            data = sd.split(',')
            data = [i.strip(r'\n') for i in data]
            std_data = Stores.objects.get_or_create(name=data[0], address=data[1], \
                                                    contact_no=data[2], landmark=data[3], \
                                                    email=data[4], location=data[5])

        return HttpResponse("Added store details")


def get_store_details(request):

    data = Stores.objects.all()
    return render(request, 'store_details.html', {'store_data': data})


class StoreView(ListView):

    model = Stores
    query_set = Stores.objects.all()
    template_name = 'store_details.html'
    context_object_name = 'store_data'
    ordering = 'name'


def success(request):
    return render(request, 'success.html')


def add_details_using_form(request):
    import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            #Simport pdb;pdb.set_trace()
            obj = Stores()
            obj.name = form.cleaned_data['name']
            obj.address = form.cleaned_data['address']
            obj.landmark = form.cleaned_data['landmark']
            obj.email = form.cleaned_data['email']
            obj.location = form.cleaned_data['location']
            obj.contact_no = form.cleaned_data['contact_no']
            obj.save()
        else:
            raise form.ValidationErrors
        return HttpResponseRedirect(reverse('success'))
    else:
        form = StoreForm()

    return render(request, 'add_details.html', {'form': form})


'''class AddStoreDetailsView(FormView):
    template_name = 'add_details.html'
    form_class = StoreForm
    success_url = '/success'

    def form_valid(self, form):
        import pdb;pdb.set_trace()
        #details = Stores.objects.get_or_create()
        form.save()
        #form.save(for_list=details)
        #return redirect(details)
        return redirect(self.success_url)'''


class AddProductsView(FormView):

    template_name = 'products.html'
    form_class = ProductsForm
    success_url = '/success'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class ProductsView(ListView):

    model = Products
    query_set = Products.objects.all()
    template_name = 'products_details.html'
    context_object_name = 'products_data'


@cache_page(10*60)
def no_of_visits(request):
    visit = request.session.get('visits', 0)
    request.session['visits'] = visit + 1
    return render(request, 'store_details.html', {'visits': request.session['visits']})
















