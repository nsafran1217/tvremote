import tvremote
from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])    # Get the size of data
        post_data = self.rfile.read(content_length)  # Get the data


        post_text = post_data.decode("utf-8")  #convert raw bytes to text
        action = (post_text.split("&")[0]).split("=")[1] #split first param
        sleeptime = (post_text.split("&")[1]).split("=")[1] #and second


        if action == 'Power': #call functions in tvremote with correct action
            result = tvremote.PowerOff()
        if action == 'VolDown':
            result = tvremote.VolDown()
        if action == 'Sleep':
            result = tvremote.Sleep(sleeptime)
        
        print(result)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        response = BytesIO()

        response.write(str.encode(str(result)))
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('tv.nsafran.com', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
