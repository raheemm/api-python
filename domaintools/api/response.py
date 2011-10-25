import json
from   domaintools.utils import obj

class Response:

    def __init__(self, request=None):
        #if isinstance(request, Request):
        #    raise ServiceException(ServiceException.INVALID_REQUEST_OBJECT)
        self.jsonObject = None
        self.request    = request
        self.mergeJson(request.raw_response)

    def mergeJson(self, raw=None):
        self.jsonObject = obj(json.loads(raw))


    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            try:
                return object.__getattribute__(self.jsonObject.response, name)
            except AttributeError:
                return None

