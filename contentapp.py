#!/usr/bin/python3

import webapp

class contentPutApp (webapp.webApp):

    content = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        method = request.split(' ')[0]
        resource = request.split(' ')[1]
        try:
            body = request.split('\r\n\r\n')[1]
        except IndexError:
            body = None
        return (method, resource, body)

    def process(self, splittedRequest):
        if splittedRequest[0] == 'GET':
            if splittedRequest[1] in self.content.keys():
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[splittedRequest[1]] \
                    + "</body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
            return (httpCode, htmlBody)
        else:
            self.content[splittedRequest[1]] = splittedRequest[2]
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[splittedRequest[1]] \
                + "</body></html>"
            return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = contentPutApp("localhost", 1234)
