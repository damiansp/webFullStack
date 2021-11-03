from http.server import BaseHTTPRequestHandler, HTTPServer


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebserverHandler)
        print(f'Web server running on port {port}')
        server.serve_forever()
    except KeyboardInterrupt:
        print('User stopping server...')
        server.socket.close()


class WebserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = b''
                output += b'<html><body>Hello!</body></html>'
                self.wfile.write(output)
                print(output)
                return
        except IOError:
            self.send_error(404, f'File Not Found: {self.path}')


if __name__ == '__main__':
    main()
