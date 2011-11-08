from domaintools.api.request       import Request

"""
 EXAMPLE - 2 different calls bringing the same result
 service: whois
 type   : json
 domain : domaintools.com
"""
if __name__ == "__main__":

    # call 1
    print Request().service('whois').domain('domaintools.com').withType('json').execute() + '\n'

    # call 2
    print Request().service('whois').domain('domaintools.com').toJson().execute() + '\n'

