import unittest
import os
import json
from   minimock                      import Mock
from   domaintools.api.configuration import Configuration
from   domaintools.api.request       import Request
from   domaintools.api.response      import Response


class TestResponse(unittest.TestCase):

    def setUp(self):
        """to execute before each test"""

        self.root_path     = os.path.realpath(os.curdir)
        self.configuration = Configuration(self.root_path+'/domaintools/conf/api.ini')
        self.request       = Request(self.configuration)

        self.request.domain('domaintools.com')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 200
        transport.get.mock_returns        = open(self.root_path + '/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        self.request.set_transport(transport)

        self.response                     = self.request.execute()



    def test_request_attached_to_response(self):
        """check Request instance has been attached to Response instance"""

        self.assertTrue(self.request == self.response.request)

