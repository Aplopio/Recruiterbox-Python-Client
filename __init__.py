from rbox import rbox as api_client
import unittest
import uuid

#'''
api_client.SITE = "http://demoaccount.rbox.com:8000"
api_client.api_key = "****************"
#'''

api_client.username = "demoaccount@recruiterbox.com"
api_client.SCHEMA_DUMP_URI = api_client.SITE+"/static/schema_dump.json"