import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agyenim_boateng.settings.base')
application = get_wsgi_application()
