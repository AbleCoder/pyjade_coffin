from pyjade_coffin.app_settings import JADE_ENABLED


if JADE_ENABLED:
    # register pyjade jinja extension
    from coffin.template.library import Library
    from pyjade.ext.jinja import PyJadeExtension

    register = Library()
    register.tag(PyJadeExtension)
