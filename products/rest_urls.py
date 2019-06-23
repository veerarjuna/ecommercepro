from django.conf.urls import url
from products.rest_views import StoreViewAPI, StoreRetrieveAPI, StoreViewSet
from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Store API')

router = DefaultRouter()
router.register('store_view', StoreViewSet)

urlpatterns = [
    url(r'store_api/', StoreViewAPI.as_view()),
    url(r'store_ret/(?P<pk>\d+)/', StoreRetrieveAPI.as_view()),
    url(r'^swag/', schema_view)
]

urlpatterns += router.urls