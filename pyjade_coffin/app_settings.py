from django.conf import settings


# turn off autoescape by default so pyjade can handle it
JINJA2_AUTOESCAPE = getattr(settings, 'PYJADE_COFFIN_JINJA2_AUTOESCAPE', False)
