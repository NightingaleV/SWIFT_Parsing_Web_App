from rest_framework import serializers
from django.utils.translation import ugettext as _

from .models import SwiftMessage


class SwiftMessageSerializer(serializers.ModelSerializer):
    direction = serializers.CharField(source='get_direction_display')
    message_type = serializers.CharField(source='message_type.type_name')
    message_type_purpose = serializers.CharField(source='message_type.purpose')

    class Meta:
        model = SwiftMessage
        fields = [
            'id', 'transaction_id', 'source_file',
            'direction', 'message_content',
            'message_type', 'message_type_purpose'
        ]
