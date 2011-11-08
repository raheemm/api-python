from domaintools.api.request       import Request

if __name__ == "__main__":

    print Request().domain('domaintools.com').toJson().execute()

