import unittest
import os
from   domaintools.api.configuration import Configuration
from   domaintools.api.request       import Request
from   domaintools.exceptions        import ServiceException

class TestRequest(unittest.TestCase):

    def get_transport(self):
        pass

    def test_transport_called_on_get(self):
        configuration = Configuration(os.path.realpath(os.curdir) + "/domaintools/conf/api.ini")
        request       = Request(configuration)
        request.withType('xml').domain('domaintools.com')
        self.assertTrue(True)

