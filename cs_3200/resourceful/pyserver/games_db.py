import sqlite3

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

class GamesDB:
    
    def __init__(self):
        self.connection = sqlite3.connect("games_db.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        
    def createGame(self, name, console, max_players, splitscreen, price):
        data = [name, console, max_players, splitscreen, price]
        self.cursor.execute("INSERT INTO games (name, console, max_players, splitscreen, price) VALUES (?, ?, ?, ?, ?)", data)
        self.connection.commit()
        
    def getAllGames(self):
        self.cursor.execute("SELECT * FROM games")
        records = self.cursor.fetchall()
        return records
        
    def getOneGame(self, game_id):
        data = [game_id]
        self.cursor.execute("SELECT * FROM games WHERE id = ?", data)
        record = self.cursor.fetchone()
        return record

    def deleteOneGame(self, game_id):
        data = [game_id]
        self.cursor.execute("DELETE FROM games WHERE id = ?", data)
        self.connection.commit()

    def editOneGame(self, game_id, name, console, maxPlayers, splitscreen, price):
        data = [name, console, maxPlayers, splitscreen, price, game_id]
        self.cursor.execute("UPDATE games SET name = ?, console = ?, max_players = ?, splitscreen = ?, price = ? WHERE id = ?", data)
        self.connection.commit()
