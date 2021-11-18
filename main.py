# Http
from http.server import HTTPServer

# Network
from network import RequestHandler


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
