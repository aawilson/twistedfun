import os
import sys

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__) ), "..", "lib", "python") )

from twistedfun.add20 import Add20Controller
from twistedfun.add20json import Add20JSONController

PORT = 8888

if __name__ == "__main__":
    root = File(os.path.join("..","public"), defaultType='text/html; charset=utf-8')
    root.childNotFound = File(os.path.join("..", "public", "404.html"))
    root.putChild('add20', Add20Controller())
    root.putChild('add20json', Add20JSONController())

    factory = Site(root)
    reactor.listenTCP(PORT, factory)
    reactor.run()
