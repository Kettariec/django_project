from django.urls import path
from catalog.views import home, contacts, product_card
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_card/', product_card, name='product_card')
    ]
