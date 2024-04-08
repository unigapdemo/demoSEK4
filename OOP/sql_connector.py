import mysql.connector
import ABC

class BaseDatabase(ABC):
    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute_query(self, query, params=None):
        pass

    def fetch_query(self, query, params=None):
        pass

class MongoDBDatabase(BaseDatabase):
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.database = database
        self.client = None

    def connect(self):
        self.client = pymongo.MongoClient(self.host, self.port)

    def disconnect(self):
        self.client.close()

    def execute_query(self, query, params=None):
        db = self.client[self.database]
        db.command(query)

    def fetch_query(self, query, params=None):
        db = self.client[self.database]
        result = db.command(query)
        return result

class MySQLDatabase(BaseDatabase):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        cursor.close()

    def fetch_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

# Example usage:
db = MySQLDatabase(host='localhost', user='your_username', password='your_password', database='your_database')
db.connect()

# Execute a query
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

# Insert data
insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
insert_data = ("John Doe", "john@example.com")
db.execute_query(insert_query, insert_data)

# Fetch data
select_query = "SELECT * FROM users"
users = db.fetch_query(select_query)
for user in users:
    print(user)

# Disconnect from the database
db.disconnect()
