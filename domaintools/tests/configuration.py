import unittest
import os
from   domaintools.api.configuration import Configuration
from   domaintools.exceptions        import ServiceException

class TestConfiguration(unittest.TestCase):

    def test_default_config_called_if_none_given(self):

        default_config_path = os.path.realpath(os.curdir) + "/api.ini"
        configuration              = Configuration();
        self.assertTrue(default_config_path==configuration.default_config_path);


    def test_service_exception_if_config_file_do_not_exists(self):
        try:
            configuration = Configuration('invalid_path')
        except Exception as e:
            self.assertTrue(True)

    def test_merge_with_default_confguration(self):
        config = {"username":"username", "key":"password"}
        configuration = Configuration(config)

        self.assertTrue(configuration.username==config['username'] and configuration.password==config['key'])


    def test_service_exception_if_empty_username(self):
        try:
            configuration = Configuration({'username':''})
        except ServiceException as e:
            self.assertTrue(True)


    def test_service_exception_if_empty_key(self):
        try:
            configuration = Configuration({'username':'username', 'key':''})
        except ServiceException as e:
            self.assertTrue(True)

    def test_default_transport_called_if_invalid_given(self):
        configuration = Configuration({'username':'username', 'key':'password', 'transport_type':'fake'})
        default_config = configuration.default_config

        self.assertTrue(default_config['transport_type']==configuration.transport_type)

