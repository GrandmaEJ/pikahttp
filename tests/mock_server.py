from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
from urllib.parse import urlparse


class MockHandler(BaseHTTPRequestHandler):
    def _send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/get":
            response = {
                "headers": dict(self.headers),
                "url": self.path,
                "method": "GET",
            }
            self._send_json_response(response)
        elif path == "/headers":
            response = {"headers": dict(self.headers)}
            self._send_json_response(response)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        if self.path == "/post":
            try:
                json_body = json.loads(body)
            except json.JSONDecodeError:
                json_body = None

            response = {
                "headers": dict(self.headers),
                "url": self.path,
                "method": "POST",
                "json": json_body,
                "data": body,
            }
            self._send_json_response(response)
        else:
            self.send_response(404)
            self.end_headers()


class MockServer:
    def __init__(self, port=0):
        self.port = port
        self.server = HTTPServer(("localhost", port), MockHandler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True

    def start(self):
        self.server_thread.start()
        self.port = self.server.server_port
        return f"http://localhost:{self.port}"

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join()
