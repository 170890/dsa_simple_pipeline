import sqlite3

class Sqlite:
    
    def __init__(self) -> None:
      pass

    def executeSql(database: str, query: str, rows = None) -> None:
      try:
        conn = sqlite3.connect(database)
        conn.execute(query, rows)
        conn.commit()
        conn.close()
      except sqlite3.Error as e:
        print(e)

    def createTable(db: str, query: str, table: str) -> None:
      try:
        conn = sqlite3.connect(db)
        conn.execute(f'DROP TABLE IF EXISTS {table}')
        conn.execute(query)
        conn.commit()
        conn.close()
      except sqlite3.Error as e:
        print(e)