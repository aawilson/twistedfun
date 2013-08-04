import simplejson

from twisted.web.resource import Resource

class Add20JSONPage(Resource):
    def __init__(self, the_int):
        Resource.__init__(self)  # Fun fact, twisted's Resource class is an old-style class
        self.the_int = the_int

    def render_GET(self, request):
        request.setHeader("Content-Type", "application/json")

        response = {}
        response["result"] = self.the_int + 20
        return simplejson.dumps(response)


class Add20JSONController(Resource):
    def getChild(self, childName, request):
        return Add20JSONPage(int(childName))
