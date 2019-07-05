#!/usr/bin/python3
#

import socket, os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = int(os.getenv("HTTP_PORT", 8080))

httpGetResponseBody = os.getenv("HTTP_GET_RESPONSE_BODY", "HTTP OK")
httpPostResponseBody = os.getenv("HTTP_POST_RESPONSE_BODY", "HTTP Accepted")

class MyServer(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.wfile.write(bytes(httpGetResponseBody, "utf-8"))

	def do_POST(self):
		print( "Incoming http: ", self.path )

		if self.headers['Content-Length'] is not None:
			content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
			post_data = self.rfile.read(content_length) # <--- Gets the data itself
			print( "POST data: ", post_data.decode("utf-8") )

		self.send_response(204)
		self.wfile.write(bytes(httpPostResponseBody, "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
