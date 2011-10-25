# domaintoolsAPI PYTHON Wrapper #

## Presentation ##

The domaintoolsAPI PYTHON Wrapper is a simple connector to access all webservices of [domaintools.com](http://domaintools.com "domaintools.com").

## Getting started ##

1- Clone the project with Git by running:

    $ git clone git://github.com/DomainTools/api-python

2- Rename the **api.ini.default** to **api.ini**

3- Fill **api.ini**  with your domaintools credentials:

    username  = 'your_api_username';
    key       = 'your_api_key';

3-A Create a short PHP file which requires the DomaintoolsAPI.class.php and makes a simple call to a webservice (**whois** for example):

```python
  import domaintools.api.request

  # Make a call to the webservice whois with a xml return
  # type for the domain name : domaintools.com

  request  = Request().service("whois").withType("xml").domain("domaintools.com") // Call the request
  response = request.execute();
  print response;
```

