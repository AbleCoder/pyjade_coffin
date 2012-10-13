import os

from coffin.common import CoffinEnvironment
from app_settings import JINJA2_AUTOESCAPE


__all__ = ('env',)

env = None

class PyjadeCoffinEnvironment(CoffinEnvironment):
    """Override join_path() to enable relative template paths."""
    def join_path(self, template, parent):
        return os.path.normpath(os.path.join(os.path.dirname(parent), template))

def get_env():
    """
    :return: A Jinja2 environment singleton.
    """
    from django.conf import settings

    kwargs = {
        'autoescape': JINJA2_AUTOESCAPE,
    }
    kwargs.update(getattr(settings, 'JINJA2_ENVIRONMENT_OPTIONS', {}))

    result = PyjadeCoffinEnvironment(**kwargs)
    # Hook Jinja's i18n extension up to Django's translation backend
    # if i18n is enabled; note that we differ here from Django, in that
    # Django always has it's i18n functionality available (that is, if
    # enabled in a template via {% load %}), but uses a null backend if
    # the USE_I18N setting is disabled. Jinja2 provides something similar
    # (install_null_translations), but instead we are currently not
    # enabling the extension at all when USE_I18N=False.
    # While this is basically an incompatibility with Django, currently
    # the i18n tags work completely differently anyway, so for now, I
    # don't think it matters.
    if settings.USE_I18N:
        from django.utils import translation
        result.install_gettext_translations(translation)

    return result

env = get_env()
