import pymysql


class SqlConnector:
    def __init__(self, user, password, database, host):
        # Connect to the database
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)
        
        self.connection.cursor 


    def run_query(self, query, params=None, expect_result=False):

        with self.connection.cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if expect_result:
                return cursor.fetchall()
            else: 
                self.connection.commit()


    def insert_data(self, table: str, values: tuple, columns:list):
        """
        Executes insert statement to database

        """
        
        value_params = ','.join(['%s']*len(values))
        columns = ','.join(x for x in columns)
        query = f"INSERT INTO {table}({columns}) VALUES({value_params});"
        self.run_query(query, values)
        
