"""Run the static UI and the same Vercel handler locally."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from api.budget import handler


class DevHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent / "public"), **kwargs)

    def do_POST(self):
        if self.path == "/api/budget":
            handler.do_POST(self)
        else:
            self.send_error(404)

    respond = handler.respond


if __name__ == "__main__":
    print("용돈 기입장: http://127.0.0.1:8872", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8872), DevHandler).serve_forever()
