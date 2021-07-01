from rest_framework import serializers
from django.utils.translation import ugettext as _

from .models import SwiftMessage


class SanctionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftMessage
        fields = ['id', 'transaction_id', 'source_file',
                  'direction', 'message_content', 'message_type']
