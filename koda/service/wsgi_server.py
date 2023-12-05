import warnings
import koda.http


def application(environ, start_response):

    warnings.warn("The WSGI application entrypoint moved from "
                  "odoo.service.wsgi_server.application to odoo.http.root "
                  "in 15.3.",
                  DeprecationWarning, stacklevel=1)
    return koda.http.root(environ, start_response)
