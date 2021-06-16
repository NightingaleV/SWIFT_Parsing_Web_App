from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView, UpdateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Customer


# Create your views here.
class IndexView(TemplateView):
    template_name = 'pages/index.html'


class CustomerList(ListView):
    model = Customer
    context_object_name = 'customer_list'
    template_name = 'pages/customer_list.html'
    # paginate_by = 10


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['full_name']
    template_name = 'pages/create_customer.html'
    success_url = reverse_lazy('swift_parsing_app:customer-list')
