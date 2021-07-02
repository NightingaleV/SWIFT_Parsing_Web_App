from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView, UpdateView, DetailView, ListView, CreateView
from django.urls import reverse_lazy
from swift_parsing_app.models import SwiftMessage, SourceFile, SwiftField, SwiftFieldValueDetail, \
    SwiftFieldValue, MessageType
from swift_parsing_app.forms import FileFieldForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'pages/index.html'


class DashboardView(ListView):
    model = SwiftMessage
    context_object_name = 'swift_messages'
    template_name = 'pages/customer_list.html'
    # paginate_by = 10
#
#
# class CustomerCreateView(CreateView):
#     model = Customer
#     fields = ['full_name']
#     template_name = 'pages/create_customer.html'
#     success_url = reverse_lazy('swift_parsing_app:customer-list')


class UploadSwiftCSVFile(FormView):
    template_name = 'pages/upload_swift_file.html'
    form_class = FileFieldForm
    success_url = reverse_lazy('sanctions_screening:upload-customer-file-success')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        uploaded_file = files[0]
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
