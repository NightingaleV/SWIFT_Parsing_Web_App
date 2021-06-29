from django.urls import path
from django.urls import path, include, reverse
from django.views.generic import TemplateView

from .views import IndexView, UploadSourceCSVFile

app_name = 'swift_parsing_app'

# UI Pages
general_urlpatterns = [
    path('', IndexView.as_view(), name='home-page'),
    # path('dashboard-react/', ListSanctionAlertsReactApp.as_view(), name='dashboard-react'),
    # path('archive/', ListCloseSanctionAlerts.as_view(), name='alert-archive'),
    # path('alert/<uuid:sanction_alert_id>/', UpdateSanctionAlerts.as_view(), name='update-sanction-alert'),
    # path('customer/<uuid:customer_id>/', CustomerDetail.as_view(), name='customer-detail'),
    # path('react-homepage/', TemplateView.as_view(template_name='pages/react.html'),
    #      name='react-home'),
]

# Static pages
supporting_urlpatterns = [
    path('upload-customer-file/success',
         TemplateView.as_view(template_name='pages/static/upload_success_page.html'),
         name='upload-swift-file-success'),

]

# API Access points
api_urlpatterns = [
    # path('api/', include('swift_parsing_app.api.router')),
    path('upload-customer-file/', UploadSourceCSVFile.as_view(), name='upload-customer-file'),
]

urlpatterns = general_urlpatterns + supporting_urlpatterns + api_urlpatterns