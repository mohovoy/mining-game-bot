import sqlite3

class Database:

    def __init__(self, db_name, client):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.client = client

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER NOT NULL UNIQUE,
            miners INTEGER DEFAULT 0,
            money INTEGER DEFAULT 1000,
            level INTEGER DEFAULT 1,
            xp INTEGER DEFAULT 0
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
            id INTEGER PRIMARY KEY UNIQUE,
            name VARCHAR(100) NOT NULL UNIQUE,
            cost INTEGER NOT NULL,
            power INTEGER NOT NULL,
            req_lvl INTEGER NOT NULL
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS miners (
            user_id INTEGER,
            miner_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(miner_id) REFERENCES shop(id)
        )""")

        for guild in self.client.guilds:
            for member in guild.members:
                if self.cursor.execute(f"SELECT id FROM users WHERE id = {member.id}").fetchone() is None:
                    self.cursor.execute(f"INSERT INTO users(id) VALUES ('{member.id}')")
                    self.connection.commit()
                else:
                    pass

    def getUserInformation(self, user):
        return self.cursor.execute(f"SELECT computers, money, level, xp FROM users WHERE id = {user}").fetchall()[0]