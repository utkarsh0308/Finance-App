import pyodbc

class DbConnUtil:
     
    server = r'LAPTOP-VHF8SO2V'
    database = 'Finance_Management_System'  

    connection_string = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'Trusted_Connection=yes;'
    )

    @staticmethod
    def getConnection():
        try:
            # Accessing the class variable 'connection_string' using the class name
            conn = pyodbc.connect(DbConnUtil.connection_string)
            return conn
        except pyodbc.Error as e:
            print(f"Failed to connect to database: {e.args}")
