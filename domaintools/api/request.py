class Request:

    def __init__(self, configuration=None):

        self.configuration           = None
        self.service_name            = ''
        self.return_type             = None
        self.authorized_return_types = ['json', 'xml', 'html']
        self.url                     = None
        self.options                 = []
        self.domain_name             = None
        self.raw_response            = None

        if(configuration == None):
            self:configuration = Configuration()
        else:
            self:configuration = configuration

