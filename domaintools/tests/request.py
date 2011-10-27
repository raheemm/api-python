import unittest
import os
import json
from   domaintools.api.configuration import Configuration
from   domaintools.api.request       import Request
from   domaintools.exceptions        import ServiceException
from   domaintools.exceptions        import BadRequestException
from   domaintools.exceptions        import NotAuthorizedException
from   domaintools.exceptions        import InternalServerErrorException
from   domaintools.exceptions        import ServiceUnavailableException
from   domaintools.utils             import load_config_file
from   minimock                      import Mock

class TestRequest(unittest.TestCase):

    def setUp(self):
        """to execute before each test"""

        self.root_path = os.path.realpath(os.curdir)

    def test_transport_called_on_get(self):
        """test transport is really called"""

        configuration = Configuration(self.root_path + "/api.ini")
        request       = Request(configuration)
        request.withType('json').domain('domaintools.com')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 200
        transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        request.set_transport(transport)

        try:
            request.execute()
        except Exception as e:
            pass

        self.assertTrue(transport.get_status()==200)


    def test_json_call_if_unknown_return_type(self):
        """check ServiceException raised if unknown return_type"""

        request = Request().withType('unknownType').domain('domaintools.com')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 200
        transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        request.set_transport(transport)

        self.assertTrue(json.loads(request.execute())!= None)


    def test_service_exception_if_invalid_options(self):
        """check ServiceException raised if invalid options"""

        try:
            request = Request().where('invalidOptions').execute()
        except ServiceException as e :
            self.assertTrue(True)


    def test_add_credentials_for_unsecure_authentication(self):
        """check username and key are really added to options"""

        config = load_config_file(self.root_path+'/api.ini')
        configuration = Configuration(config)
        configuration.secure_auth = False

        request = Request(configuration)
        request.add_credentials_options()

        options = request.get_options()

        self.assertTrue(config['username']==options['api_username'] and config['key']==options['api_key'])


    def test_not_authorized_request_exception(self):
        """test NotAuthorizedException raised for status code 403"""

        request = Request().withType('json').domain('domaintools')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 403
        transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        request.set_transport(transport)

        try:
            request.execute()
        except NotAuthorizedException as e:
            self.assertTrue(True)

        def test_bad_request_exception(self):
            """test BadRequestException raised for status code 400"""

            request = Request().withType('json').domain('domaintools')

            transport                         = Mock('RestService')
            transport.get_status.mock_returns = 400
            transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
            request.set_transport(transport)

            try:
                request.execute()
            except BadRequestException as e:
                self.assertTrue(True)


        def test_not_found_request_exception(self):
            """test NotFoundException raised for status code 404"""

            request = Request().withType('json').domain('domaintools')

            transport                         = Mock('RestService')
            transport.get_status.mock_returns = 404
            transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
            request.set_transport(transport)

            try:
                request.execute()
            except NotFoundRequestException as e:
                self.assertTrue(True)


    def test_internal_server_error_exception(self):
        """test InternalServerErrorException raised for status code 500"""

        request = Request().withType('json').domain('domaintools')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 500
        transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        request.set_transport(transport)

        try:
            request.execute()
        except InternalServerErrorException as e:
            self.assertTrue(True)


    def test_service_unavailable_exception(self):
        """test ServiceUnavailableException raised for status code 503"""

        request = Request().withType('json').domain('domaintools')

        transport                         = Mock('RestService')
        transport.get_status.mock_returns = 503
        transport.get.mock_returns        = open(self.root_path + '/domaintools/tests/fixtures/domain-profile/domaintools.com/good.json').read()
        request.set_transport(transport)

        try:
            request.execute()
        except ServiceUnavailableException as e:
            self.assertTrue(True)

