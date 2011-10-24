from configuration import Configuration
import hmac
import hashlib
from datetime      import datetime
from ..exceptions  import ServiceUnavailableException

class Request:

    def __init__(self, configuration=None):

        self.configuration           = None
        self.service_name            = ''
        self.return_type             = None
        self.authorized_return_types = ('json', 'xml', 'html')
        self.url                     = None
        self.options                 = {}
        self.domain_name             = ''
        self.raw_response            = None

        if(configuration == None):
            self.configuration = Configuration()
        else:
            self.configuration = configuration


    def service(self, service_name=''):
        self.service_name = service_name
        return self

    def withType(self, return_type):
        self.return_type = return_type
        return self

    def domain(self, domain_name=''):
        self.domain_name = domain_name
        return self

    def where(self, options):
        if type(options) is not dict:
            raise ServiceException(ServiceException.INVALID_OPTIONS)
        return self


    def query(self, query):
        return self.where({'query':query})


    def add_credentials_options(self):

        api_username = self.configuration.username
        api_key      = self.configuration.password

        self.options['api_username'] = api_username

        if self.configuration.secure_auth:
            timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

            uri       = '/' + self.configuration.sub_url
            if self.domain_name.strip()=='':
                uri   = uri + '/'
            else:
                uri   = uri + '/' + self.domain_name
            uri       = uri + self.service_name

            self.options['timestamp'] = timestamp
            params                    = ''.join([api_username, timestamp, uri])
            self.options['signature'] = hmac.new(api_key, params, digestmod=hashlib.sha1).hexdigest()

    def get_service_name(self):
        return self.serice_name

    def get_options(self):
        return self.options

    def set_transport(self, transport):
        self.configuration.transport = transport

    def get_return_type(self):

        if self.return_type != None:
            return_type = self.return_type
        else:
            return_type = self.configuration.return_type

        return return_type

    def build_options(self):
        self.options['format'] = self.get_return_type()
        self.add_credentials_options()


    def build_url(self):
        query_string = ''
        for k, v in self.options.iteritems():
            query_string = query_string + k + '=' + v + '&'
        query_string = query_string.strip('& ')
        self.url     = self.configuration.base_url + ('/' if self.domain_name.strip()=='' else '/' + self.domain_name + '/') + '?' + query_string


    def execute(self, debug=0):
        raw_response = ''
        self.build_options()

        if self.return_type==None:
            self.options['format'] = 'json'

        self.build_url()

        if debug==1: return self.url

        self.raw_response = self.request()

        if self.return_type==None:
            return Response(self, self.raw_response)

        return self.raw_response

    def debug(self):
        return self.execute(1)

    def request(self):
        transport = self.configuration.transport
        response=''
        try:
            response = transport.get(self.url)
        except Exception as e:
            print e
            #raise ServiceUnavailableException()

        status = transport.get_status()

        if status==200:
            return response
        elif status==400:
            raise BadRequestException()
        elif status==403:
            raise NotAuthorizedException()
        elif status==404:
            raise NotFoundException()
        elif status==500:
            raise InternalServerErrorException()
        elif status==503:
            raise ServiceUnavailableException()
        else:
            raise ServiceException('Empty response')

