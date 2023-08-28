from src.Ingestion import Ingestion

def main():
    new_ingestion = Ingestion()
    new_ingestion.createDatabase('mydb.db')
    new_ingestion.ingestData()

if __name__ == "__main__":
    main()