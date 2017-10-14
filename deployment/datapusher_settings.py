import uuid

DEBUG = False
TESTING = False
SECRET_KEY = str(uuid.uuid4())
USERNAME = str(uuid.uuid4())
PASSWORD = str(uuid.uuid4())

NAME = 'datapusher'

# database

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/job_store.db'

# webserver host and port

HOST = '0.0.0.0'
PORT = 8800

# logging

#FROM_EMAIL = 'server-error@example.com'
#ADMINS = ['yourname@example.com']  # where to send emails

#LOG_FILE = '/tmp/ckan_service.log'
STDERR = True


def get_row_set(table_set):
    """Return the table called "data" or the first table in the set."""
    names = [r.name.lower() for r in table_set.tables]
    try:
        return table_set.tables[names.index('data')]
    except ValueError:
        return table_set.tables[0]


GET_ROW_SET = get_row_set
