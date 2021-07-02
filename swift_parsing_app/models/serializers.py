from rest_framework import serializers
from django.utils.translation import ugettext as _

from .models import SourceFile, SwiftMessage, SwiftFieldValue


class SourceFileSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    total_msg_ctn = serializers.IntegerField()

    class Meta:
        model = SourceFile
        fields = ['id', 'file_name', 'status', 'created_at', 'total_msg_ctn']


class SwiftMessageSerializer(serializers.ModelSerializer):
    direction = serializers.CharField(source='get_direction_display')
    message_type = serializers.CharField(source='message_type.type_name')
    message_type_description = serializers.CharField(source='message_type.description')
    message_type_purpose = serializers.CharField(source='message_type.purpose')

    class Meta:
        model = SwiftMessage
        fields = [
            'id', 'transaction_id', 'source_file',
            'direction', 'message_content',
            'message_type', 'message_type_purpose', 'message_type_description'
        ]


class SourceFileDetailSerializer(serializers.ModelSerializer):
    pass
    status = serializers.CharField(source='get_status_display')
    swift_messages = SwiftMessageSerializer(many=True, read_only=True)
    total_msg_ctn = serializers.IntegerField()

    class Meta:
        model = SourceFile
        fields = ['id', 'file_name', 'status', 'created_at', 'total_msg_ctn', 'swift_messages']


class SwiftFieldValueSerializer(serializers.ModelSerializer):
    swift_message_id = serializers.CharField(source='swift_message.id')
    swift_field_id = serializers.CharField(source='swift_field.id')
    swift_field_meta_tag = serializers.CharField(source='swift_field.key_mt_tag')
    swift_field_tag = serializers.CharField(source='swift_field.field_tag')
    swift_field_name = serializers.CharField(source='swift_field.field_name')
    swift_field_status = serializers.CharField(source='swift_field.get_status_display')
    swift_field_content_options = serializers.CharField(source='swift_field.content_options')
    swift_field_description = serializers.CharField(source='swift_field.description')
    swift_field_value_is_empty = serializers.SerializerMethodField()

    class Meta:
        model = SwiftFieldValue
        fields = [
            'id', 'swift_message_id', 'swift_field_id', 'swift_field_name', 'swift_field_meta_tag', 'swift_field_tag',
            'swift_field_status', 'swift_field_content_options', 'swift_field_description', 'swift_field_value_is_empty'
            , 'field_value'
        ]

    def get_swift_field_value_is_empty(self, obj):
        return obj.field_value is None
