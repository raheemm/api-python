from domaintools.api.request       import Request

"""
 EXAMPLE - 3 different calls bringing the same result
 service: whois
 type   : json
 domain : domaintools.com
"""
if __name__ == "__main__":

    # call 1
    print Request().service('whois').domain('domaintools.com').withType('json').execute() + '\n'

    # call 2
    print Request().service('whois').domain('domaintools.com').withType('json').execute() + '\n'

    # call 3
    response = Request().service('whois').domain('domaintools.com').execute()
    print response.toJson() + '\n'

