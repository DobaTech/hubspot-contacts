from six import text_type
from voluptuous import Schema


CONTACT_LIST_SCHEMA = Schema(
    {'listId': int, 'name': text_type, 'dynamic': bool},
    required=True,
    extra=True,
    )


CONTACT_LIST_MEMBERSHIP_UPDATE_SCHEMA = \
    Schema({'updated': list}, required=True, extra=True)
