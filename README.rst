=============
pyjade-coffin
=============

Jade_ and Jinja2_ template support for Django using PyJade_'s Jinja2 extension
with Coffin_.

PyJade's Django template loader lacks mixin functionality due to the fact
Django has no macro support. This package uses Coffin with PyJade's Jinja2
extension to overcome this. It also provides a few fixes/tweaks to make jade's
behavior in Django more closely match the native JavaScript jade engine.

What this package does:

* Registers PyJade's Jinja2 extension with coffin so ``.jade`` files are rendered
  though Jinja2 which gives us mixin support.

* Add relative path include support by subclassing ``coffinEnvironment`` and 
  overriding the ``join_path`` method. This matches jade's native JavaScript
  engine's behavior.

* Sets Jinja2's autoescape to ``false`` which allows HTML escaping to be handled
  in Jade templates.

Installation
============

Install Package
---------------
Install with pip::

    pip install pyjade-coffin


Setup Django
------------
Add ``coffin`` and ``pyjade-coffin`` to *INSTALLED_APPS* in ``settings.py``::

    INSTALLED_APPS = (
    ...
        'coffin',
        'pyjade_coffin',
    ...
    )


Usage
=====

Shortcut Render Functions
-------------------------
To render a jade/jinja2 template you can use the render functions in the
``pyjade_coffin.shortcuts`` module provides:

* render_to_response
* render
* render_to_string

These functions work just like django.shortcuts_' render functions except
they render Jade and Jinja2 templates.

**NOTE:** Jade templates are detected by their file extension so only
``*.jade`` files get processed by PyJade.

Here is an example view::

    from django.template import RequestContext
    from pyjade_coffin.shortcuts import render_to_response


    def test_jade(request):
        c = RequestContext(request, {
            'test': ['this', 'is', 'test', 'data'],
            'check': "<em>Autoescape Test</em>",
        })

        return render_to_response('test_page.jade', c)



.. _django.shortcuts: https://docs.djangoproject.com/en/dev/topics/http/shortcuts/
.. _Coffin: https://github.com/coffin/coffin
.. _Jade: http://jade-lang.com/
.. _Jinja2: http://jinja.pocoo.org/docs/
.. _PyJade: https://github.com/SyrusAkbary/pyjade
