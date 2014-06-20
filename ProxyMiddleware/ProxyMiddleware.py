#!/usr/bin/env python
#
# Reverse Proxy Middleware. This snippit of code sets the script_name environment variable to what is set in nginx
# It then strips the common bits from the PATH_INFO variable

from bottle import redirect, HTTPError, abort

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

class TrailingSlash(object):
    def __init__(self, wrap_app):
        self.wrap_app = wrap_app
        self.wrap_app = self.app = wrap_app

    def __call__(self, environ, start_response):
        try:
            self.app.router.match(environ)
        except HTTPError:
            PI = environ['PATH_INFO']
            environ['PATH_INFO'] = PI + '/'
            try:
                self.app.router.match(environ)
                start_response('301 Redirect', [('Location', environ['SCRIPT_NAME'] + environ['PATH_INFO']),])
                return []
            except:
                environ['PATH_INFO'] = PI
                pass
        return self.wrap_app(environ, start_response)

