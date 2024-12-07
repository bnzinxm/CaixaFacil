import yaml

class Database:
    def __init__(self, HOST, PORT, USER, PASSWORD, NAME):
        self.host = HOST
        self.port = PORT
        self.user = USER
        self.password = PASSWORD
        self.name = NAME
    
    def load_config(self, yaml_file: str):
        with open(yaml_file, "r") as file:
            config = yaml.safe_load(yaml_file)
            self.file = config 
            db_config = self.file.get("database", {})
            
            Database.HOST = db_config.get("host")
            Database.PORT = db_config.get("port")
            Database.USER = db_config.get("user")
            Database.PASSWORD = db_config.get("password")
            Database.NAME = db_config.get("name")

    def get_host(yaml_file):
        database = yaml_file.get("database", {})
        return database.get("host", "Isso não existe!")

    def get_port(yaml_file):
        database = yaml_file.get("database", {})
        return database.get("port", "Isso não existe!")

    def get_user(yaml_file):
        database = yaml_file.get("database", {})
        return database.get("user", "Isso não existe!")

    def get_password(yaml_file):
        database = yaml_file.get("database", {})
        return database.get("password", "Isso não existe!")

    def get_name(yaml_file):
        database = yaml_file.get("database", {})
        return database.get("name", "Isso não existe!")