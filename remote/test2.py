import tvremote
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length)  # Get the data


        post_text = post_data.decode("utf-8") 
        action = (post_text.split("&")[0]).split("=")[1]
        sleeptime = (post_text.split("&")[1]).split("=")[1]


        if action == 'Power':
            tvremote.PowerOff()
        if action == 'VolDown':
            tvremote.VolDown()
        if action == 'Sleep':
            tvremote.Sleep(sleeptime)
        

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = BytesIO()

        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(post_data)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
