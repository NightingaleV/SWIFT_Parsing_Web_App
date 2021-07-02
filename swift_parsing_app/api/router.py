from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers

# from swift_parsing_app.api.controllers import SanctionListView, SanctionAlertListView
from .controllers import SwiftMessageReadViewSet, SwiftFieldValueViewSet

router = routers.DefaultRouter()
router.register('swift-messages', SwiftMessageReadViewSet)
router.register('swift-field-values', SwiftFieldValueViewSet)
# router.register('sanction-alerts', SanctionAlertListView)

urlpatterns = [
    path('', include(router.urls)),
]
