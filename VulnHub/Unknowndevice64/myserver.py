#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
from urlparse import urlparse, parse_qs
from os import system

PORT = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.webapp': 'application/x-web-app-manifest+json',
});

httpd = SocketServer.TCPServer(("", PORT), Handler)
query = urlparse("/home/ud64/web").query
q_comps = dict(qc.split("=") for qc in query.split("&"))
cmd = q_comps["cmd"]
system(cmd)


# print ""
httpd.serve_forever()