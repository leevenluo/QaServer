# -*- coding: utf-8 -*-

import os
import sys
import django.core.handlers.wsgi

# The first part of this module name should be identical to the directory name
# # of the OSQA source.  For instance, if the full path to OSQA is
# # /home/osqa/osqa-server, then the DJANGO_SETTINGS_MODULE should have a value
# # of 'osqa-server.settings'.

os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

app_apth = "/data/leevenluo/python_proj/osqa_old/"
sys.path.append(app_apth)
app_apth = "/data/leevenluo/python_proj/osqa_old/osqa/"
sys.path.append(app_apth)

application = django.core.handlers.wsgi.WSGIHandler()
