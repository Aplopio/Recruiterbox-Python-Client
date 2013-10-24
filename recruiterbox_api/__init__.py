import pytasty
import unittest
import uuid
import requests
from StringIO import StringIO

class DetailDocResource(pytasty.DetailResource):
    """
    This is a special case
    """

    def get_file(self):
        self._update_object()
        response = requests.get(pytasty.__API_OBJ__.SITE + self.location)
        response = requests.get(response.content)
        buff = StringIO()
        buff.content_type = response.headers['content-type']
        buff.name = self.filename
        buff.write(response.content)
        buff.seek(0)
        #buff.close()
        return buff

    def delete(self):
        raise Exception("Cannot delete file direct!")

    def save(self, **kwargs):
        #TODO: POST self.file to the proper file
        pass

class ListDocResource(pytasty.ListResource):

    _detail_class = DetailDocResource

    def all(self, **kwargs):
        return []

    def get_detail_object(self, json_obj, dehydrate_object=True):
        return super(ListDocResource,self).get_detail_object(json_obj, dehydrate_object=True)

    def _generate_detail_class(self):
        return super(ListDocResource,self)._generate_detail_class()

    def create(self, file_tuple, **kwargs):
        """Requires a tuple -- (filename, content, content_type)"""
        doc = super(ListDocResource,self).create(**kwargs)
        doc.file = file_tuple
        return doc


recruiterbox_api = pytasty.PyTasty(resource_custom_list_class={"docs":ListDocResource})
