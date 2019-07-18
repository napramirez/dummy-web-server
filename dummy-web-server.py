#!/usr/bin/python3
#

import socket, os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = int(os.getenv("HTTP_PORT", 8080))

httpGetResponseBody = os.getenv("HTTP_GET_RESPONSE_BODY", "HTTP OK")
httpPostResponseBody = os.getenv("HTTP_POST_RESPONSE_BODY", "HTTP Accepted")

httpPostResponseCode = os.getenv("HTTP_POST_RESPONSE_CODE", "202")

httpPostResponseHeaderLocation = os.getenv("HTTP_POST_RESPONSE_HEADER_LOCATION")

httpResponseHeaderContentType = os.getenv("HTTP_RESPONSE_HEADER_CONTENT_TYPE", "*/*")
httpResponseHeaderAccept = os.getenv("HTTP_RESPONSE_HEADER_ACCEPT", "*/*")

class MyServer(BaseHTTPRequestHandler):

	def do_GET(self):
		response = bytes(httpGetResponseBody, "utf-8")

		self.send_response(200)
		self.send_header("Content-Length", str(len(response)))
		self.end_headers()
		self.wfile.write(response)

	def do_POST(self):
		if self.headers['Content-Length'] is not None:
			content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
			post_data = self.rfile.read(content_length) # <--- Gets the data itself
			sys.stdout.write("POST data: " + post_data.decode("utf-8") + "\n")

		response = bytes(httpPostResponseBody, "utf-8")

		self.send_response(int(httpPostResponseCode))
		self.send_header("Content-Length", str(len(response)))

		if httpResponseHeaderContentType:
			self.send_header("Content-Type", httpResponseHeaderContentType)

		if httpResponseHeaderAccept:
			self.send_header("Accept", httpResponseHeaderAccept)

		if httpPostResponseHeaderLocation:
			self.send_header("Location", httpPostResponseHeaderLocation)

		self.end_headers()
		self.wfile.write(response)

myServer = HTTPServer((hostName, hostPort), MyServer)
sys.stdout.write(str(time.asctime()) + "Server Starts - " + hostName + ":" + str(hostPort) + "\n")

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
sys.stdout.write(str(time.asctime()) + "Server Stops - " + hostName + ":" + str(hostPort) + "\n")
