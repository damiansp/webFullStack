import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem


print('Initializing database connection...')
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


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
    FORM = b'''                                                       
    <form method="POST" enctype="multipart/form-data" action="/hello">
      <h2>What would you lke to say?</h2>
      <input name="message" type="text" />
      <input type="submit" value="Submit" />
    </form>'''

    def do_GET(self):
        try:
            for page in ['/hello', '/hola']:
                if self.path.endswith(page):
                    self._populate_page(page)
            if self.path.endswith('/restaurants'):
                self._list_restaurants()
        except IOError:
            self.send_error(404, f'File Not Found: {self.path}')

    def _populate_page(self, ending):
        text = {
            '/hello': b'Hello!',
            '/hola': b'&#161Hola!'
        }[ending]
        if text != b'Hello!':
            text += b' <a href="/hello">Back to Hello</a>'
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        output = b''
        output += b'<html><body>' + text
        output += self.FORM
        output += b'</body></html>'
        self.wfile.write(output)
        print(output)
        return

    def _list_restaurants(self):
        try:
            print('Getting restaurant list')
            restaurants = session.query(Restaurant).all()
            print('restaurants:', restaurants)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = '<html><body>'
            for r in restaurants:
                output += f'<h2>{r.name}</h2></br></br>'
            output += '</body></html>'
            output = bytes(output, encoding='utf-8')
            self.wfile.write(output)
            print(output)
            return
        except:
            raise
        

    def do_POST(self):
        try:
            self.send_response(302)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message_content = fields.get('message')
            print('content:', message_content[0])
            output = b''
            output += b'<html><body>'
            output += b'<h2>Ok, how\'s this: </h2>'
            output += bytes(f'<h1>{message_content[0]}</h1>', 'utf-8')
            output += self.FORM
            output += b'</body></html>'
            self.wfile.write(output)
            print(output)
        except:
            raise
            

if __name__ == '__main__':
    main()
