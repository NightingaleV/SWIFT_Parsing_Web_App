from django.urls import path
from django.views.generic import TemplateView

from .views import IndexView, CustomerCreateView, CustomerList

app_name = 'swift_parsing_app'
urlpatterns = [
    path('', IndexView.as_view(), name='home-page'),
    path('customer-list/', CustomerList.as_view(), name='customer-list'),
    path('create-customer/', CustomerCreateView.as_view(), name='create-customer'),
]
