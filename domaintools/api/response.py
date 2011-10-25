import json
from   domaintools.utils import obj

class Response:

    def __init__(self, request=None):
        #if isinstance(request, Request):
        #    raise ServiceException(ServiceException.INVALID_REQUEST_OBJECT)
        self.json       = None
        self.jsonObject = None
        self.request    = request
        self.mergeJson(request.raw_response)

    def mergeJson(self, raw=None):
        jsonObject = obj(json.loads(raw))
        if(jsonObject == None): raise ServiceException()

        self.json       = raw
        self.jsonObject = jsonObject

    def __getattr__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            try:
                return object.__getattribute__(self.jsonObject.response, name)
            except AttributeError:
                return None

    def toJson(self, refresh=False):
        if refresh==True:
            json = self.request.withType('json').execute()
            self.mergeJson(json)
        return self.json


    def toObject(self):
        return obj(self.toJson())

    def toXml(self):
        return self.request.withType('xml').execute()

    def toHtml(self):
        return self.request.withType('html').execute()

