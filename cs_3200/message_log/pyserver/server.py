from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
from dummydb import DummyDB
import json

# MY_GAMES = ["Minecraft", "Monster Hunter", "Rock Band", "Animal Crossing"]

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not found.", "utf-8"))
        
    def handleGetGamesCollection(self):
        # response status code
        self.send_response(200)
        # response header
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        
        self.end_headers()
        # response body
        db = DummyDB('mydatabase.db')
        allRecords = db.readAllRecords()
        print(allRecords)
        self.wfile.write(bytes(json.dumps(allRecords), "utf-8"))
            
    def handleCreateMovie(self):
        print("request headers:", self.headers)
        
        # 1. read data in the request body
        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode("utf-8")
        print("raw request body:", request_body)
        parsed_body = parse_qs(request_body)
        print("parsed body:", parsed_body)
        
        # 2. save name to the "database"
        movie_name = parsed_body["name"][0] # index the dictionary and list
        db = DummyDB('mydatabase.db')
        db.saveRecord(movie_name)
   
        
        # 3. send a response
        self.send_response(201) # successfully created
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
    
    def do_GET(self):
        if self.path == "/hello":
            # response status code
            self.send_response(200)
            # response header
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            # response body
            self.wfile.write(bytes("Hello, world.", "utf-8"))
        
        elif self.path == "/games":
            self.handleGetGamesCollection()
        
        else:
            self.handleNotFound()
    
    def do_POST(self):
        if self.path == "/games":
            self.handleCreateMovie()
        else:
            self.handleNotFound()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    
    listen = ("127.0.0.1", 8080)
    server = ThreadedHTTPServer(listen, MyRequestHandler)
    
    print("Server running!")
    server.serve_forever()
    
if __name__ == '__main__':
    run()
    