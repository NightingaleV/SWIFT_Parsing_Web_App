from rest_framework import viewsets
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from swift_parsing_app.models import SwiftMessage, SwiftFieldValue
from swift_parsing_app.models.serializers import SwiftMessageSerializer, SwiftFieldValueSerializer


class SwiftMessageReadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SwiftMessage.objects.all()
    serializer_class = SwiftMessageSerializer

    @action(detail=True, methods=['get'])
    def related_field_values(self, request, pk=None):
        related_field_values = SwiftFieldValue.select.related_field_values(swift_message_pk=pk)
        serializer = SwiftFieldValueSerializer(related_field_values, many=True)
        return Response(serializer.data)


class SwiftFieldValueViewSet(viewsets.ModelViewSet):
    queryset = SwiftFieldValue.objects.all()
    serializer_class = SwiftFieldValueSerializer
