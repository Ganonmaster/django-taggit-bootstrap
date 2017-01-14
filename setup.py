#!/usr/bin/env python

from distutils.core import setup

setup(name='django-taggit-bootstrap',
      version='0.2',
      description='Django Taggit widget with autosuggest support on top of Bootstrap 3 - updated with latest bootstrap-tagsinput',
      author='Hidde Jansen',
      author_email='hidde@hiddejansen.com',
      url='https://github.com/Ganonmaster/django-taggit-bootstrap',
      packages=['taggit_bootstrap'],
      package_data={'taggit_bootstrap':["templates/taggit_bootstrap/*.html","static/css/*.css","static/js/*.js"]},
      requires=['django_taggit']
     )
