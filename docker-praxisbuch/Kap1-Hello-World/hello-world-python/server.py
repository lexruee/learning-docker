import os 
from  datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World Python!</title>
</head>
<body>
    <h1>Hello World Python!</h1>
    <ul>
        <li>Server time: {time}</li>
        <li>Server load: {load}</li>
    </ul>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        load = os.getloadavg()
        time = datetime.now().astimezone()
        page_html = PAGE_HTML.format(time=time, load=load[0])
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_html, "utf-8"))

def run():
    addr = ('', 8080)
    httpd = HTTPServer(addr, MyHandler)
    httpd.serve_forever()

run()
