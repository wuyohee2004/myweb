#!/usr/bin/env python
#Author: Alex Li
import sys,os
#import tri_config
#sys.path.append(tri_config.Working_dir)
sys.path.append('C:/xampp/htdocs/myweb')
os.environ['DJANGO_SETTINGS_MODULE'] ='myweb.settings'
import django
django.setup()
#----------------Use Django Mysql model----------------
from poll.models import *
