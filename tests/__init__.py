from recruiterbox_api import recruiterbox_api as recruiterbox
import unittest
import uuid

#'''
recruiterbox.SITE = "http://demoaccount.rbox.com:8000"
recruiterbox.api_key = "**************************"
#'''

recruiterbox.username = "demoaccount@recruiterbox.com"
recruiterbox.SCHEMA_DUMP_URI = recruiterbox.SITE+"/static/schema_dump.json"