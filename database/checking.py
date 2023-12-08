#importing necessary modules
import pathlib
import sqlite3
import pandas as pd

#use pathlib to get current working directory
path = pathlib.Path().cwd()

#Define a function to create a SQLite database
def create_db(database_name, filename, table_name):
    # create a path to the data file
    file_path = path / filename

    # create a connection to the database
    con = sqlite3.connect(database_name)
    # create a cursor
    cur = con.cursor() 

    #Read data from the CSV file
    retails = pd.read_csv(file_path)
    #insert the data into the specified table 
    retails.to_sql(table_name, con, index = False, if_exists = 'replace')    
     
    # execute a select statement as f-string and print results to verify insertion
    results = cur.execute(f"SELECT * FROM {table_name}").fetchall()
    print(results)
    # commit the changes to the database
    con.commit()
    # close the connection
    con.close()


if __name__=="__main__":
    #parameters for creating database
    database_name = "Retail.db"
    filename = "retail_store.csv"
    table_name = "retails"
    #Call create_db function with specified parameters
    create_db(database_name, filename, table_name)
    
