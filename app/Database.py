import sqlite3

class Database:

    def __init__(self, databaseName):
        self.name = databaseName
        self.connection = sqlite3.connect(self.name + '.db')
        self.conn = self.connection.cursor()

    def create(self, tableName, props):
        self.conn.execute("""CREATE TABLE general ()""")

    def add(self, where, what):
        pass

    def update(self, where, what):
        pass

    def remove(self, where, what):
        pass

    def get(self, where, what):
        pass
