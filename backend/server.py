import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

PORT = 5000

# Kết nối PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="vtfzmzvq_project2_db",
    user="vtfzmzvq_project2_user",
    password=".Dung@))$"
)
cur = conn.cursor()

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/hello':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            
            # Truy vấn DB
            cur.execute("SELECT message FROM messages LIMIT 1;")
            row = cur.fetchone()
            message = row[0] if row else "No data in DB"
            
            self.wfile.write(json.dumps({"message": message}).encode())
        else:
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('0.0.0.0', PORT), SimpleHandler)
print(f"Backend running on port {PORT}")
httpd.serve_forever()
