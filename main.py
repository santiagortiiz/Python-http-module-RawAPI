''' Server Setup '''

# Standard libraries
import json

# Http 
from http.server import HTTPServer, BaseHTTPRequestHandler

# Network
from network import map

# Serializer
from serializer import to_bytes

class RequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, response_code=200):
        ''' Send basic response arguments '''
        self.send_response(response_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        ''' Handler for requests with GET method '''

        self._set_response()

        match = map.routematch(self.path)
        params, _ = match
        controller = params.pop('controller') 

        response = controller(**params)
        response = to_bytes(response)

        self.wfile.write(response)

    def do_POST(self):
        ''' Handler for requests with POST method '''

        self._set_response()
        
        # Get the length of the body
        content_length = int(self.headers['Content-Length'])

        # Read the body of the request
        body = self.rfile.read(content_length) 
        response = to_bytes(body)
        self.wfile.write(json.dumps(response).encode())


if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 8000

    httpd = HTTPServer((HOST, PORT), RequestHandler)
    print(f'Server listening at http://{HOST}:{PORT} \nUse <Ctrl-C> to stop')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        # Is left a fake http request to close
        httpd.server_close()
        print('server stopped')
