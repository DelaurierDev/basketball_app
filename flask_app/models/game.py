from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
mydb = 'basketball_db'

class Game:
    def __init__(self,data):
        self.id = data['id']
        self.hometeam = data['hometeam']
        self.homescore = data['homescore']
        self.awayteam = data['awayteam']
        self.awayscore = data['awayscore']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
