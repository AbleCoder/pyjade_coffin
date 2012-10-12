"""
pyjade-coffin
~~~~~~~~~~~~~

pyjade-coffin is a package that adds `jade <http://jade-lang.com/>` template
rendering to django using `PyJade <https://github.com/SyrusAkbary/pyjade>`'s
Jinja2 extension through `coffin <https://github.com/coffin/coffin>`.

:copyright: 2012 by Brandon Orther
:license: MIT, see LICENSE for more details.
"""


__all__ = ('__version__', '__build__', '__docformat__', 'get_revision')
__version__ = (0, 1, '0', 'dev')
__docformat__ = 'restructuredtext en'

import os

def _get_git_revision(path):
    revision_file = os.path.join(path, 'refs', 'heads', 'master')
    if not os.path.exists(revision_file):
        return None
    fh = open(revision_file, 'r')
    try:
        return fh.read()
    finally:
        fh.close()

def get_revision():
    """
    :returns: Revision number of this branch/checkout, if available. None if
        no revision number can be determined.
    """
    package_dir = os.path.dirname(__file__)
    checkout_dir = os.path.normpath(os.path.join(package_dir, '..'))
    path = os.path.join(checkout_dir, '.git')
    if os.path.exists(path):
        return _get_git_revision(path)
    return None

__build__ = get_revision()
