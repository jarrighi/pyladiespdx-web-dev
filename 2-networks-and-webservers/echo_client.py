#!/usr/bin/env python

import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
  """ A simple echo client """

  # Create a TCP/IP socket for the client
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect the client socket to the socket on the server
  server_address = (host, port)
  print "Connecting to %s port %s" % server_address
  sock.connect(server_address)

  # Send data
  try:
    message = "Test message. This will be echoed"
    print "Sending %s" % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
      data = sock.recv(16)
      amount_received += len(data)
      print "Received: %s" % data

  # In case there was a problem, print the error details
  except socket.errno, e:
    print "Socket error: %s" %str(e)
  except Exception, e:
    print "Other exception: %s" %str(e)
  
  # Close connection with the server
  finally:
    print "Closing connection to the server"
    sock.close()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Socket Server Example')
  # Specify a port to connect with on the server
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()
  port = given_args.port

  # Run the client!
  echo_client(port)