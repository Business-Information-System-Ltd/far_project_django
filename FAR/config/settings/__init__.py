import pymysql

pymysql.install_as_MySQLdb()
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENVIRONMENT = os.environ.get('DJANGO_ENV', 'dev')

if ENVIRONMENT == 'production':
    from .prod import *
else:
    from .dev import *