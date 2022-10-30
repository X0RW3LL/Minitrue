#!/usr/bin/env python3

import http.server
import socketserver

def serve(PORT, DIRECTORY, interface, filename):
    '''
    Simple Python HTTP Server
    
    Parameters:
    PORT (int): PORT number to start listening on
    DIRECTORY (str): Path to start serving
    '''
    class Handler(http.server.SimpleHTTPRequestHandler):
        # Credit: https://stackoverflow.com/a/60658958
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=DIRECTORY, **kwargs)

    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('\n[+] Serving \033[32m{}\033[0m at port \033[32m{}\033[0m'.format(DIRECTORY, PORT))
        if PORT != 80:
            print('\n[+] Payload URL: http://{}:{}/{}\n'.format(interface, PORT, filename))
        else:
            print('\n[+] Payload URL: http://{}/{}\n'.format(interface, filename))
        httpd.serve_forever()

