from .base import *

import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    "de-identifier-7cb0b8229b7c.herokuapp.com"
]

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=True,
    ),
}
