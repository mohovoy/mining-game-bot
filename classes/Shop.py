from classes.Database import Database


class Shop(Database):
    
    def getAllMashines(self):
        return self.cursor.execute("SELECT * FROM shop").fetchall()

    def addMashine(self, name, cost, power, req_lvl):
        self.cursor.execute(f"INSERT INTO shop('name', 'cost', 'power', 'req_lvl') VALUES ('{name}', {cost}, {power}, {req_lvl})")
        self.connection.commit()