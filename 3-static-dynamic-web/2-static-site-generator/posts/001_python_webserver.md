# Writing Webservers in Python

It's a lot of fun! Here's how to do it.

```
import argparse

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
class RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path == "/hi":
      try:
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        # add additional headers here, if you'd like. For example: 
        # self.send_header('X-silly-header', 'cheese')
        self.end_headers()
        self.wfile.write("Hello from server!\n")
      except IOError:
        self.send_error(404, "File Not Found: %s" % self.path)

def run_server(host, port):
  try:
    server = HTTPServer((host, port), RequestHandler)
    print 'Starting httpserver at http://{}:{}'.format(host,port)
    print '(Press CTRL+C to quit)'
    server.serve_forever()
  except KeyboardInterrupt:
    server.socket.close()  


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='HTTP Server')
  parser.add_argument('--port', action="store", dest="port", type=int, default=8000)
  parser.add_argument('--host', action="store", dest="host", type=str, default='127.0.0.1')
  given_args = parser.parse_args()
  port = given_args.port
  host = given_args.host

  run_server(host, port)
```