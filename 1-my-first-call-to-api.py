from domaintools.api.request       import Request

if __name__ == "__main__":

    response = Request().domain('domaintools.com').execute()
    print response.toJson()

