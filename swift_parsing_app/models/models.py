import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .mixins import CreationModificationDateMixin


class SourceFile(models.Model, CreationModificationDateMixin):
    IN_PROGRESS = 1
    PROCESSED = 2

    FILE_STATUSES = [
        (IN_PROGRESS, _('Processing in progress')),
        (PROCESSED, _('File processed')),
    ]

    file_name = models.CharField(max_length=128, null=False)
    status = models.PositiveSmallIntegerField(blank=True, choices=FILE_STATUSES)
    file_content = models.TextField()

    class Meta:
        db_table = 'source_file'


class MessageType(models.Model, CreationModificationDateMixin):
    CUSTOMER_PAYMENTS = 1
    FINANCIAL_INSTITUTION_TRANSFER = 2
    TREASURE_MARKETS = 3
    CASH_LETTERS = 4
    SECURITIES = 5
    COMMODITIES = 6
    DOCUMENTARY_CREDIT = 7
    TRAVELLER_CHEQUES = 8
    CASH_MANAGEMENT = 9
    MSG_CATEGORIES = [
        (CUSTOMER_PAYMENTS, _('Customer Payments and Cheques')),
        (FINANCIAL_INSTITUTION_TRANSFER, _('Financial Institution Transfers')),
        (TREASURE_MARKETS, _('Treasury Markets - Foreign Exchange, Money Markets and Derivatives')),
        (CASH_LETTERS, _('Collections and Cash Letters')),
        (SECURITIES, _('Securities Markets')),
        (COMMODITIES, _('Treasury Markets - Commodities')),
        (DOCUMENTARY_CREDIT, _('Documentary Credits and Guarantees/Standby Letters of Credit')),
        (TRAVELLER_CHEQUES, _('Travellers Cheques')),
        (CASH_MANAGEMENT, _('Cash Management and Customer Status')),
    ]

    category = models.PositiveSmallIntegerField(blank=True, choices=MSG_CATEGORIES)
    type_name = models.CharField(max_length=64, null=False)
    purpose = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField()

    class Meta:
        db_table = 'message_type'


class SwiftMessage(models.Model, CreationModificationDateMixin):
    INCOMING = 1
    OUTGOING = 2
    MSG_DIRECTION = [
        (INCOMING, _('Incoming')),
        (OUTGOING, _('Outgoing')),
    ]
    transaction_id = models.UUIDField(editable=True)
    source_file_id = models.ForeignKey(SourceFile, related_name='swift_messages', on_delete=models.CASCADE)
    direction = models.PositiveSmallIntegerField(blank=True, choices=MSG_DIRECTION)
    message_content = models.TextField()
    message_type_id = models.ForeignKey(MessageType, related_name='swift_messages', on_delete=models.CASCADE)
    basic_header = models.CharField(max_length=64, null=True, blank=True)
    application_header = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'swift_message'


class SwiftField(models.Model, CreationModificationDateMixin):
    key_mt_tag = models.CharField(max_length=16, blank=True)
    message_type_id = models.ForeignKey(MessageType, related_name='swift_fields', on_delete=models.CASCADE)
    field_tag = models.CharField(max_length=16, blank=False)
    field_name = models.CharField(max_length=64, blank=False)

    MANDATORY = 1
    OPTIONAL = 2
    STATUSES = [
        (MANDATORY, _('Mandatory')),
        (OPTIONAL, _('Optional')),
    ]
    status = models.PositiveSmallIntegerField(blank=True, choices=STATUSES)
    content_options = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        ordering = ['message_type_id', 'field_tag']
        db_table = 'swift_field'


class SwiftFieldValue(models.Model, CreationModificationDateMixin):
    swift_message_id = models.ForeignKey(SwiftMessage, related_name='swift_values', on_delete=models.CASCADE)
    swift_field_id = models.ForeignKey(SwiftField, related_name='swift_values', on_delete=models.CASCADE)
    field_value = models.CharField(max_length=512, null=True)

    class Meta:
        db_table = 'swift_field_value'


class SwiftFieldValueDetail(models.Model, CreationModificationDateMixin):
    swift_field_value_id = models.ForeignKey(SwiftFieldValue, related_name='swift_detailed_values',
                                             on_delete=models.CASCADE)
    detailed_value = models.CharField(max_length=512, null=True)
