#!/usr/bin/env python3
"""
MANASA Events - Local Server
Opens automatically at http://localhost:8000
Press Ctrl+C to stop.
"""

import http.server
import socketserver
import webbrowser
import os
import threading

PORT = 8000

# Always serve from the folder this script is in
FOLDER = os.path.dirname(os.path.abspath(__file__))
os.chdir(FOLDER)

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Redirect root "/" to index.html
        if self.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, format, *args):
        print(f"  >> {self.path}")

def open_browser():
    import time
    time.sleep(1.2)
    webbrowser.open(f"http://localhost:{PORT}/index.html")

print("=" * 50)
print("   MANASA Events - Local Server")
print("=" * 50)
print(f"\n  Serving folder : {FOLDER}")
print(f"  URL            : http://localhost:{PORT}")
print("\n  Browser will open automatically...")
print("  Press Ctrl+C to stop.\n")
print("-" * 50)

threading.Thread(target=open_browser, daemon=True).start()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n  Server stopped.")
