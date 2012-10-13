from django.conf import settings


# turn off jinja2 autoescape by default so pyjade can handle it
JINJA2_AUTOESCAPE = getattr(settings, 'PYJADE_COFFIN_JINJA2_AUTOESCAPE', False)

# enable jade support (by register pyjade extension) by default
JADE_ENABLED = getattr(settings, 'PYJADE_COFFIN_JADE_ENABLED', True)
