"""
WSGI config for koalixcrm project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'koalixcrmprod.settings.production_docker_postgres_settings')
application = get_wsgi_application()
