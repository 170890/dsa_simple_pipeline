import csv
from src.helper.Sqlite import Sqlite

class Ingestion:

    def __init__(self) -> None:
        pass

    def remove_dot(self,value):
        return int(round(float(value.replace('.','')), 0))
    
    def createDatabase(self, database: str) -> None:
        
        try:
            query = '''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER,
                    margem_lucro REAL
                )'''
            Sqlite.createTable(database,query, 'producao')
        except:
            print("Failed to create database !!")
    
    def ingestData(self) -> None:
        
        database = 'mydb.db'
        
        try:
            with open('data/producao_alimentos.csv', 'r') as file:

                reader = csv.reader(file)
                
                next(reader)

                for row in reader:
                    if int(row[1]) > 10:

                        row[3] = self.remove_dot(row[3])

                        profit_margin = round((row[3] / float(row[1])) - float(row[2]), 2)

                        query = 'INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)'
                        rows = (row[0], row[1], row[2], row[3], profit_margin)
                        Sqlite.executeSql(database, query, rows)
                
                print("Ingestion completed")
        except:
            print("Failed to ingest !!")

    