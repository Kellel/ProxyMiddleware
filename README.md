ProxyMiddleware
===============

A shim for wsgi applications behind nginx

A common problem that I have ran into when hosting wsgi applications behind a nginx reverse proxy is the rewriting of urls being returned from the upstream server.

This little bit of wsgi middleware will rewrite the script name variable based on a variable set in your nginx config.

Add this line to your nginx config:

    proxy_set_header X-SCRIPT-NAME /path;
    
And this line to your wsgi file:

    application = ReverseProxied(application)


*Note:* Variations of this code exist in other places on the internet. I do not claim to be the person who came up with this. I just love it and need somewhere I can easily find it.
