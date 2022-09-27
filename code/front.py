from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request

hostName = "localhost"
serverPort = 80


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>Citations</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" %
                         self.get_citation(), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    def get_citation(self):
        with urllib.request.urlopen('http://localhost:8080') as response:
            message = response.read()
            return message.decode('utf-8')


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.shutdown()
    webServer.server_close()
    print("Server stopped.")