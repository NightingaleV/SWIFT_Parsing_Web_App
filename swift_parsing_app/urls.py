from django.urls import path
from django.views.generic import TemplateView

from .views import IndexView


app_name = 'swift_parsing_app'
urlpatterns = [
    path('', IndexView.as_view(), name='home-page'),
]