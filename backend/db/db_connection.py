class DBConnection:
    def __init__(self, dbtype, url, config=None):
    
        self.db_type = dbtype.lower()
        self.url = url

        if self.db_type == "supabase" or self.db_type == "postgresql":
            self.sql_connect()
        elif self.db_type == "firebase":
            self.nosql_connect(config)
        else:
            print(f"{self.db_type} is not a supported db type")

    def sql_connect(self):
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        import psycopg2

        engine = create_engine(self.url)

        self.sql_conn = engine.connect()

        return self.sql_conn

    def sql_close(self):
        self.sql_conn.close()

    def nosql_connect(self, config):
        pass

