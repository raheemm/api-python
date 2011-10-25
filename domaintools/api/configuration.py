import os
from domaintools                import utils
from domaintools.exceptions     import ServiceException
from domaintools.transport.curl import CurlRestService

class Configuration:

    def __init__(self, ini_resource = None):
        """
        Construct the class
        Initiliaze it with default values (if no config given)
        """
        self.host                = None
        self.port                = None
        self.sub_url             = None
        self.base_url            = None
        self.username            = None
        self.password            = None
        self.secure_path         = None
        self.return_type         = None
        self.transport_type      = None
        self.transport           = None
        self.default_config_path = None
        self.default_config      = {

            'username'       : '',
            'key'            : '',
            'host'           : 'api.domaintools.com',
            'version'        :'v1',
            'port'           :'80',
            'secure_auth'    : 1,
            'return_type'    : 'json',
            'transport_type' : 'curl',
            'content_type'   : 'application/json'
        }

        self.transport_map = {
            'curl'           : CurlRestService
        }

        self.default_config_path = os.path.realpath(os.curdir)+'/domaintools/conf/api.ini'

        if(ini_resource == None):
            ini_resource = self.default_config_path

        config = {}

        if(type(ini_resource) is dict):
            config = ini_resource
        else:
            config = utils.load_config_file(ini_resource)

        self.init(config)

    def validateParams(self, config):
        """
        Validate options from a given array
        Merge with the default configuration
        """
        config = dict(self.default_config,**config)

        if config['username'].strip() == '':
            raise ServiceException(ServiceException.EMPTY_API_USERNAME)

        if config['key'].strip() == '':
            raise ServiceException(ServiceException.EMPTY_API_KEY)

        try:
            transport = self.transport_map[config['transport_type']]()
        except Exception as e:
            config['transport_type'] = self.default_config['transport_type'];

        #if implements(transport, Transport) == 0:
        #    config['transport_type'] = self.default_config['transport_type'];

        return config


    def init(self, config):

        config                         = self.validateParams(config);

        self.host 	                   = config['host'];
        self.port					   = config['port'];
        self.sub_url				   = config['version'];
        self.username				   = config['username'];
        self.password				   = config['key'];
        self.secure_auth               = True if config['secure_auth'] in ('True','true','1') else False;
        self.return_type 		       = config['return_type'];
        self.content_type			   = config['content_type'];
        self.transport_type            = config['transport_type'];

        self.base_url				   = 'http://' + self.host +':' + self.port + '/' + self.sub_url;

        self.transport                 = self.transport_map[config['transport_type']](self.content_type)

