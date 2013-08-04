from twisted.web.resource import Resource


class Add20Page(Resource):
    def __init__(self, the_int):
        Resource.__init__(self)  # Fun fact, twisted's Resource class is an old-style class
        self.the_int = the_int

    def render_GET(self, request):
        return "<!doctype html><html><head><title>Adding 20 to %d</title></head><body>The result is %d!</body></html>" % (
            self.the_int,
            self.the_int + 20
            )


class Add20Controller(Resource):
    def getChild(self, childName, request):
        return Add20Page(int(childName))
