This is a dumb server written in twisted web.

If you run this, and make a request to the port specified in twistedfun-server.py (default 8888), it will attempt to serve up a page according to the following rules:

1. If it matches `"../add20/<someinteger>"`, it will give a simple html page with the integer + 20
2. If it matches `"../add20json/<someinteger>"`, it will give the same thing, but in JSON
3. It it doesn't match those two routes, it will attempt to serve up something from the public directory. If the route is `"../"` (a.k.a. root), it will serve index.html.
4. Anything else, it will serve up 404.html
