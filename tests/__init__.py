from recruiterbox_api import recruiterbox_api as recruiterbox
import unittest
import uuid



recruiterbox.SITE = "https://app.recruiterbox.com"
recruiterbox.api_key = "71831d7a84efc294ec1ab7251abac9c809c32c36"
#'''
recruiterbox.SITE = "http://demoaccount.rbox.com:8000"
recruiterbox.api_key = "8187e6418f2f93e85c10f6c2cf2eb4e96464c68e"
#'''

recruiterbox.username = "demoaccount@recruiterbox.com"
recruiterbox.SCHEMA_DUMP_URI = recruiterbox.SITE+"/static/schema_dump.json"

def get_uuid():
    return uuid.uuid4().hex

class DocResource(unittest.TestCase):

    def test_all(self):
        assert recruiterbox.docs.all() == []

    # def test_get_file(self):
    #     # candidate = recruiterbox.candidates.retrieve(id=1094488)
    #     candidate = recruiterbox.candidates.create()
    #     candidate.first_name = "api_client_test_case"
    #     candidate.last_name = get_uuid()
    #     candidate.save()

    #     doc = recruiterbox.candidates.create()
    #     resume = candidate.resume.get_file()
    #     import ipdb; ipdb.set_trace()
