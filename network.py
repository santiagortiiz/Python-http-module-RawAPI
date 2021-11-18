# Standard libraries
import json

# Http 
from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()

        response = {
            'GET': 'hello GET'
        }
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        self._set_response()

        response = {
            'POST': 'hello POST'
        }
        self.wfile.write(json.dumps(response).encode())
