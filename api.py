from domaintools.api.request       import Request
from domaintools.api.configuration import Configuration

if __name__ == "__main__":
    #print Request().service('whois').withType('xml').domain('domaintools.com').execute()

    response = Request().service('whois').domain('domaintools.com').execute()
    print response.registrant
    #print response.registration.created

