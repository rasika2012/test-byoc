from http.server import BaseHTTPRequestHandler, HTTPServer
from svgwrite import Drawing
from svgwrite.shapes import Circle
import io


class SvgCircleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/circle.svg':
            # Create a new SVG drawing
            drawing = Drawing(size=('100%', '100%'))

            # Add a circle shape
            circle = Circle(center=(50, 50), r=40)
            circle.fill('red')
            drawing.add(circle)

            # Render the SVG drawing to a string
            svg_str = drawing.tostring()

            # Send the SVG file to the client
            self.send_response(200)
            self.send_header('Content-type', 'image/svg+xml')
            self.end_headers()
            self.wfile.write(svg_str.encode('utf-8'))
        else:
            # Return a 404 error for any other request
            self.send_error(404)

if __name__ == '__main__':
    PORT = 8000
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SvgCircleHandler)
    print(f'Serving on port {PORT}')
    httpd.serve_forever()
