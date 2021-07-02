from rest_framework import viewsets
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from swift_parsing_app.models import SwiftMessage
from swift_parsing_app.models.serializers import SwiftMessageSerializer


class SwiftMessageReadView(viewsets.ReadOnlyModelViewSet):
    queryset = SwiftMessage.objects.all()
    serializer_class = SwiftMessageSerializer
