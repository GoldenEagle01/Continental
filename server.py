#!/usr/bin/env python
import BaseHTTPServer
import os
import time
import urlparse
from posixpath import basename, dirname

HOST_NAME = ''
PORT_NUMBER = 1234

speedFile = os.getcwd() + "/speed.txt"
directionFile = os.getcwd() + "/direction.txt"

def writeFile(path, content):
    target = open(path, 'w')
    target.truncate()
    target.write(str(content))
    return content

#writeFile(speedFile, 6.8)
#writeFile(directionFile, 7.3)

def main():
    createServer()

class Handler( BaseHTTPServer.BaseHTTPRequestHandler ):
    def do_GET( self ):
        response = ""
        parsed_path = self.path
        user_path = parsed_path.split('/')

        if(1 < len(user_path)):
            action = user_path[1]
        else:
            action = False

        if(2 < len(user_path)):
            function = user_path[2]
        else:
            function = False 

        if(3 < len(user_path)):
            argument1 = user_path[3]
        else:
            argument1 = False

        if(4 < len(user_path)):
            argument2 = user_path[4]
        else:
            argument2 = False            
        
        if(action == "speed"):
            writeFile(speedFile, function)

        if(action == "direction"):
            writeFile(directionFile, function)                 
        
        self.send_response(200)
        self.send_header( 'Content-type', 'text/html' )
        self.end_headers()
        self.wfile.write( response )

def createServer():
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), Handler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

if __name__ == '__main__':
    main()
