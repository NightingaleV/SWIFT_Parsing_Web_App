import os
import sys
import pandas
import random
import pytz
import pandas as pd
import uuid
import django
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.config.local')
django.setup()

from swift_parsing_app.models import SourceFile, MessageType, SwiftMessage, SwiftField, SwiftFieldValueDetail, \
    SwiftFieldValue

# Columns: MT;Status;Tag;Field_Name;Content_Options;KeyMTTag
swift_fields_df = pandas.read_csv('../../mock/SM.csv', sep=';')
swift_messages_df = pandas.read_pickle('../../mock/output_dataframe.pkl')


def populate_swift_msg_types():
    list_of_msg_types = swift_fields_df['MT'].unique()
    list_of_msg_types = sorted(list_of_msg_types)

    for msg_type in list_of_msg_types:
        new_object = MessageType.objects.get_or_create(type_name=msg_type)
    print('Message Types were created')


def populate_swift_fields():
    for row_index, row in swift_fields_df.iterrows():
        mandatory = 1 if row['Status'] == 'M' else 2
        msg_type = MessageType.objects.filter(type_name=row['MT']).first()
        swift_field = SwiftField.objects.get_or_create(key_mt_tag=row['KeyMTTag'], field_name=row['Tag'],
                                                       field_tag=row['Field_Name'], status=mandatory,
                                                       content_options=row['Content_Options'],
                                                       message_type=msg_type)

    print('Swift Fields were created')


def populate_source_file():
    source_file = SourceFile.objects.get_or_create(file_name='test_file_001.csv', status=2)
    print('Source Files were created')
    pass


def populate_swift_message():
    list_of_msgs = swift_messages_df['transaction_id'].unique()
    list_of_msgs = sorted(list_of_msgs)

    source_file = SourceFile.objects.first()

    for transaction_id in list_of_msgs:
        direction = swift_messages_df[
            (swift_messages_df['transaction_id'] == transaction_id) & (swift_messages_df['field_name'] == 'Direction')][
            'field_value'].item()
        direction_value = 1 if direction == 'I' else 2

        application_header = swift_messages_df[
            (swift_messages_df['transaction_id'] == transaction_id) & (swift_messages_df['field_name'] == '2')][
            'field_value'].item()

        msg_type = swift_messages_df[
            (swift_messages_df['transaction_id'] == transaction_id) & (swift_messages_df['field_name'] == 'MT')][
            'field_value'].item()
        msg_type_object = MessageType.objects.filter(type_name=msg_type).first()
        # transaction_id = transaction_id.replace('-','')
        new_object = SwiftMessage.objects.get_or_create(transaction_id=transaction_id, source_file=source_file,
                                                        direction=direction_value, message_type=msg_type_object,
                                                        application_header=application_header)

    print('Swift Messages were created')
    pass


def populate_swift_field_values():
    list_of_msgs = swift_messages_df['transaction_id'].unique()
    list_of_msgs = sorted(list_of_msgs)

    for transaction_id in list_of_msgs:
        transaction_object = SwiftMessage.objects.get(transaction_id=transaction_id)

        list_of_fields = swift_messages_df[swift_messages_df['transaction_id'] == transaction_id]

        for index, row in list_of_fields.iterrows():

            swift_fields_not_in_dictionary = ['Direction', 'MT', 'Rest of 2', '2', '3']
            swift_field_name = row['field_name']
            if swift_field_name not in swift_fields_not_in_dictionary:
                related_swift_field = SwiftField.objects.get(field_name=swift_field_name,
                                                             message_type=transaction_object.message_type)
                swift_field_value = row['field_value']
                new_object = SwiftFieldValue.objects.get_or_create(swift_message=transaction_object,
                                                                   swift_field=related_swift_field,
                                                                   field_value=swift_field_value)

    print('Swift Fields Values were created')
    pass


def format_db():
    # SourceFile, MessageType, SwiftMessage, SwiftField, SwiftFieldValueDetail
    SwiftFieldValueDetail.objects.all().delete()
    SwiftFieldValue.objects.all().delete()
    SwiftMessage.objects.all().delete()
    SourceFile.objects.all().delete()
    SwiftField.objects.all().delete()


#
#
# SanctionList.objects.all().delete()
# Customer.objects.all().delete()

if __name__ == '__main__':
    print("Formating the Database")
    format_db()

    populate_swift_msg_types()
    populate_swift_fields()
    populate_source_file()
    populate_swift_message()
    populate_swift_field_values()

    print('Populating Complete')
