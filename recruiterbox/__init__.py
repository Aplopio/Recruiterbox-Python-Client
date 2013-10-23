import pytasty
import unittest
import uuid

class DetailDocResource(pytasty.DetailResource):
    """
    This is a special case
    """

    def get_file(self):
        self._update_object()
        response = requests.get(rbox.SITE + self.location)
        response = requests.get(response.content)
        buff = StringIO()
        buff.content_type = response.headers['content-type']
        buff.name = self.filename
        buff.write(response.content)
        buff.seek(0)
        #buff.close()
        return buff

class ListDocResource(pytasty.ListResource):

    _detail_class = DetailDocResource

    def all(self, **kwargs):
        return []



recruiterbox = pytasty.PyTasty(resource_custom_list_class={"docs":ListDocResource})
