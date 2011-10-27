from domaintools.api.request       import Request
from domaintools.api.configuration import Configuration
import os

"""
 EXAMPLE - 3 different calls bringing the same result
 service: whois
 type   : json
 domain : domaintools.com
"""

# by default the script is waiting for an api.ini in the same directory
# if it's not the case, force the path
ini_path      = os.path.realpath(os.pardir) + "/api.ini"
configuration = Configuration(ini_path)

# call 1
print Request(configuration).service('whois').domain('domaintools.com').withType('json').execute() + '\n'

# call 2
print Request(configuration).service('whois').domain('domaintools.com').withType('json').execute() + '\n'

# call 3
response = Request(configuration).service('whois').domain('domaintools.com').execute()
print response.toJson() + '\n'

