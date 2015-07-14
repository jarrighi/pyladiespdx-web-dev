#!/usr/bin/env python

import socket
import sys
import argparse

# We'll need these variables later

# Use 0.0.0.0 for 'host' if you want to be available from other machines. 
# 'localhost' works if you're just running the client on your own machine
host = '0.0.0.0' 
data_payload = 2048
backlog = 5

def echo_server(port):
  """ A simple echo server """
  # Create a TCP socket. The first arg identifies the 'address family'.
  # We're using IPv4. AF_INET6 could be used instead for IPv6. 
  # The second arg specifies the socket type. The stream type uses TCP/IP
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Enable reuse address/port
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # Bind the socket to the port. Remember that you need both a host name/address
  # and a port to identify a socket. 
  server_address = (host, port)
  print "Starting up echo server on %s port %s" % server_address
  sock.bind(server_address)

  # Listen to clients, backlog argument specifies the max no. of queued 
  # connections
  sock.listen(backlog)
  while True:
    print "Waiting to receive message from client"

    # When a request comes in, create a new socket object that maintains a 
    # connection with the client socket
    client, address = sock.accept()

    # Get a 2048 chunk of data at a time until all of the data is received
    data = client.recv(data_payload)
    if data:
      print "Data: %s" %data

      # Send the chunk of data back to the client
      client.send(data)
      print "sent %s bytes back to %s" % (len(data), address)

      # Close the connection with the client
      client.close()

if __name__ == "__main__":
  # The next few lines (39-43) are just to get the arguments from the command 
  # that ran this script. If you're curious, check out the argparse docs
  parser = argparse.ArgumentParser(description='Socket Server Example')

  # You need to specify a port (a number larger than 1024) when you run this script 
  parser.add_argument('--port', action="store", dest="port", type=int, required=True)
  given_args = parser.parse_args()

  # Start the server on the given port!
  port = given_args.port
  echo_server(port)