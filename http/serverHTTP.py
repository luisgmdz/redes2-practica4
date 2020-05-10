from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import posixpath
import urllib.parse as urlparse
from io import BytesIO,StringIO

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        print(self.command)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_HEAD(self):
        parsed_path = parse.urlparse(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_POST(self):
        parsed_path = parse.urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        self.end_headers()

    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        resp = BytesIO()
        resp.write(b'metodo delete')
        self.wfile.write(resp.getvalue())
        
    def do_CONNECT(self):
        self.send_response(200)
        self.end_headers()
        resp = BytesIO()
        resp.write(b'metodo connect')
        self.wfile.write(resp.getvalue())

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
        resp = BytesIO()
        resp.write(b'metodo options')
        self.wfile.write(resp.getvalue())

    def do_TRACE(self):
        self.send_response(200)
        self.end_headers()
        resp = BytesIO()
        resp.write(b'metodo trace')
        self.wfile.write(resp.getvalue())
try:
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()

except Exception as e:
    print(e)
    