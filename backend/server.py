from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 5000

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            with open('data.json') as f:
                data = json.load(f)
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
print(f"Backend running on port {PORT}")
httpd.serve_forever()
