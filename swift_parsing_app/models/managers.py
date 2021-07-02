import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from datetime import datetime, timedelta
from django.db.models import Q, Prefetch, Sum, Max, Count, Case, When, Value, IntegerField, Subquery, OuterRef


class SourceFileQuerySet(models.QuerySet):
    def get_msg_count(self):
        return self.annotate(
            total_msg_ctn=Count('swift_messages')
        )


class SwiftMessageQuerySet(models.QuerySet):

    def get_msgs_from_file(self, source_file_id):
        return self.filter(source_file_id=source_file_id)

    def get_msg_ctn_for_file(self, file_id):
        return self.aggregate(related_msg_ctn=Count('pk', filter(Q(source_file_id=file_id))))


class SwiftFieldValueQuerySet(models.QuerySet):

    def related_field_values(self, swift_message_pk):
        related_field_values = self.filter(swift_message_id=swift_message_pk)
        return related_field_values
