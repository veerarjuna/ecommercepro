from django.conf.urls import url
from products.views import add_store_details, get_store_details, success, \
    add_details_using_form, StoreView, AddProductsView, ProductsView, home_view, \
    no_of_visits

urlpatterns = [
    url(r'^$', home_view, name="home"),
    url(r'store_details/', add_store_details, name="add_stores"),
    url(r'get_details/', get_store_details, name="store_details"),
    #url(r'add_details/', AddStoreDetailsView.as_view()),
    url(r'add_new_store/', add_details_using_form, name="add_store"),
    url(r'success/', success, name='success'),
    url(r'store_data/', StoreView.as_view()),
    url(r'add_prods/', AddProductsView.as_view(), name="add_prods"),
    url(r'prod_details/', ProductsView.as_view(), name="prod_details"),
    url(r'visits/', no_of_visits),
]