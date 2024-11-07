from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Log the request from Arduino
        print("Request received from Arduino")

        # Run any program or Python script
        os.system("python3 cam.py")  # execute cam.py (facial recognition)

        # Send a response back to Arduino
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        message = "Python program executed!"  # Message to display on Arduino
        self.wfile.write(message.encode("utf-8"))
        print("Sent response to Arduino")

# Set up the server
def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8080)  # Listen on port 8080
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8080...")
    httpd.serve_forever()
