import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext as _
from datetime import datetime, timedelta
from django.db.models import Q, Prefetch, Sum, Max, Count, Case, When, Value, IntegerField, Subquery, OuterRef


class SourceFileQuerySety(models.QuerySet):
    pass


class SwiftFieldValueQuerySet(models.QuerySet):

    def related_field_values(self, swift_message_pk):
        related_field_values = self.filter(swift_message_id=swift_message_pk)
        return related_field_values
