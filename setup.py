#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(name='pyjade-coffin',
    version=".".join(map(str, __import__("pyjade_coffin").__version__)),
    author='Brandon Orther',
    author_email='an.able.coder@gmail.com',
    url='http://github.com/AbleCoder/pyjade_coffin',
    license="LICENSE",
    packages=find_packages(),
    description=('Jade and Jinja2 template support for Django using PyJade\'s'
                 ' Jinja2 extension w/ coffin'),
    long_description=open('README.rst').read(),
    install_requires=[
        'Jinja2',
        'pygments',
        'coffin',
        'PyJade',
        'Django',
    ],
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
