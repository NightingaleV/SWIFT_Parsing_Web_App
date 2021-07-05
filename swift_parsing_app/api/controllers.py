from rest_framework import viewsets
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from swift_parsing_app.models import SourceFile, SwiftMessage, SwiftFieldValue
from swift_parsing_app.models.serializers import (SourceFileSerializer, SourceFileDetailSerializer,
                                                  SwiftMessageSerializer, SwiftFieldValueSerializer)
from .pagination import MessagePagination
from django.db.models import Q, Prefetch, Sum, Max, Count, Case, When, Value, IntegerField, Subquery, OuterRef


class SourceFileViewSet(viewsets.ModelViewSet):
    queryset = SourceFile.select.all()
    serializer_class = SourceFileSerializer
    pagination_class = MessagePagination

    def get_queryset(self):
        return SourceFile.select.get_msg_count()

    def get_serializer_class(self):
        if self.action == 'list':
            return SourceFileSerializer
        if self.action == 'retrieve':
            return SourceFileDetailSerializer
        return SourceFileSerializer
        # if self.action == 'retrieve':
        #     return SourceFileDetailSerializer


    @action(detail=True, methods=['get'])
    def related_messages(self, request, pk=None):
        source_file = self.get_object()
        related_msgs = SwiftMessage.select.get_msgs_from_file(source_file_id=pk)
        page = self.paginate_queryset(related_msgs)
        if page is not None:
            serializer = SwiftMessageSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = SwiftMessageSerializer(related_msgs, many=True)
        return Response(serializer.data)


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


