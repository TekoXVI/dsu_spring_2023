from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
from games_db import GamesDB
import json

# MY_GAMES = ["Minecraft", "Monster Hunter", "Rock Band", "Animal Crossing"]

class MyRequestHandler(BaseHTTPRequestHandler):
    
    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not found.", "utf-8"))
        
    def handleGetGamesCollection(self):
        db = GamesDB()
        allRecords = db.getAllGames()
        
        # response status code
        self.send_response(200)
        # response header
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        
        self.end_headers()
        # response body
        print(allRecords)
        self.wfile.write(bytes(json.dumps(allRecords), "utf-8"))
        
    def handleGetGamesMember(self, game_id):
        db = GamesDB()
        oneGame = db.getOneGame(game_id)
        
        if oneGame:
            # response status code
            self.send_response(200)
            # response header
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            
            self.end_headers()
            # response body
            print(oneGame)
            self.wfile.write(bytes(json.dumps(oneGame), "utf-8"))
        else:
            self.handleNotFound()

    def handleDeleteGamesMember(self, game_id):
        db = GamesDB()
        oneGame = db.getOneGame(game_id)
        
        if oneGame:
            # response status code
            self.send_response(200)
            # response header
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            
            self.end_headers()
            # response body
            print(oneGame, game_id)
            db.deleteOneGame(game_id)
        else:
            self.handleNotFound()
            
    # delete is just like retrieve
    # replace/update is like combining retrieve and create
            
    def handleCreateGame(self):
        print("request headers:", self.headers)
        
        # 1. read data in the request body
        length = int(self.headers["Content-Length"])
        request_body = self.rfile.read(length).decode("utf-8")
        print("raw request body:", request_body)
        parsed_body = parse_qs(request_body)
        print("parsed body:", parsed_body)
        
        # 2. save name to the "database"
        name = parsed_body["name"][0] # index the dictionary and list
        console = parsed_body["console"][0]
        max_players = parsed_body["max_players"][0]
        splitscreen = parsed_body["splitscreen"][0]
        price = parsed_body["price"][0]
        
        db = GamesDB()
        db.createGame(name, console, max_players, splitscreen, price)

        # 3. send a response
        self.send_response(201) # successfully created
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        
    def handleUpdateGamesMember(self, game_id):
        db = GamesDB()
        oneGame = db.getOneGame(game_id)
        print("editing game with this info:", oneGame)

        if oneGame:
            # parse request body
            length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(length).decode("utf-8")
            game_data = parse_qs(request_body)

            # update game information
            if "name" in game_data:
                oneGame["name"] = game_data["name"][0]
                name = oneGame["name"]
            if "console" in game_data:
                oneGame["console"] = game_data["console"][0]
                console = oneGame["console"]
            if "max_players" in game_data:
                oneGame["max_players"] = game_data["max_players"][0]
                maxPlayers = oneGame["max_players"]
            if "splitscreen" in game_data:
                oneGame["splitscreen"] = game_data["splitscreen"][0]
                splitscreen = oneGame["splitscreen"]
            if "price" in game_data:
                oneGame["price"] = game_data["price"][0]
                price = oneGame["price"]

            # save updated game information
            db.editOneGame(game_id, name, console, maxPlayers, splitscreen, price)

            # send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(oneGame), "utf-8"))
        else:
            self.handleNotFound()

        
        
        
        
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
    
        path_parts = self.path.split("/")
        if len(path_parts) == 3:
            collection_name = path_parts[1]
            member_id = path_parts[2]
        else:
            collection_name = path_parts[1]
            member_id = None
            
        if collection_name == "games":
            if member_id:
                self.handleGetGamesMember(member_id)
                
            else:
                self.handleGetGamesCollection()
            
        else:
            self.handleNotFound()
                
    
    def do_POST(self):
        if self.path == "/games":
            self.handleCreateGame()
        else:
            self.handleNotFound()
            
    def do_DELETE(self):
        path_parts = self.path.split("/")
        if len(path_parts) == 3:
            collection_name = path_parts[1]
            member_id = path_parts[2]
        else:
            collection_name = path_parts[1]
            member_id = None
            
        if collection_name == "games":
            if member_id:
                self.handleDeleteGamesMember(member_id)
            else:
                self.handleGetGamesCollection()
            
        else:
            self.handleNotFound()
            
    def do_PUT(self):
        path_parts = self.path.split("/")
        if len(path_parts) == 3:
            collection_name = path_parts[1]
            member_id = path_parts[2]
        else:
            collection_name = path_parts[1]
            member_id = None

        if collection_name == "games":
            if member_id:
                self.handleUpdateGamesMember(member_id)
            else:
                self.handleNotFound()
        else:
            self.handleNotFound()

            

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    
    listen = ("127.0.0.1", 8080)
    server = ThreadedHTTPServer(listen, MyRequestHandler)
    
    print("Server running!")
    server.serve_forever()
    
if __name__ == "__main__":
    run()
    