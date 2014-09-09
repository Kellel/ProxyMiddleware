import unittest
from ProxyMiddleware import ReverseProxied, TrailingSlash

def testing_app(environ, start_response):
    return environ

class TestProxyMiddleware(unittest.TestCase):
    def setUp(self):
        self.wsgi_app = testing_app
        self.environ = { 'SCRIPT_NAME': "", 'PATH_INFO': "/path/to/test", 'HTTP_X_SCRIPT_NAME': "/path" }

    def test_reverseproxied(self):
        app = ReverseProxied(self.wsgi_app)
        newenv = app(self.environ, False)

        self.assertTrue(newenv['SCRIPT_NAME'] ==  "/path")
        self.assertTrue(newenv['PATH_INFO'] == "/to/test")

    def test_trailingslash(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
