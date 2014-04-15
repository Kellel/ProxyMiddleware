#!/usr/bin/env python
#
# Reverse Proxy Middleware. This snippit of code sets the script_name environment variable to what is set in nginx
# It then strips the common bits from the PATH_INFO variable

class ReverseProxied(object):
 
    def __init__(self, wrap_app):
        self.wrap_app = wrap_app
        self.wrap_app = self.app = wrap_app

    def __call__ (self, environ, start_response):
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]
        return self.wrap_app(environ, start_response) 
