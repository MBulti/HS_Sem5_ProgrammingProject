import sqlite3
import sys

from sqlite3 import Connection, Cursor, Error

database_connection: Connection = None
database_cursor: Cursor = None
DB_CONNECTION_STRING = "data/database.db"

def establish_db_connection():
    """ create a database connection to a SQLite database """
    global database_connection, database_cursor
    try:
        database_connection = sqlite3.connect(DB_CONNECTION_STRING)
        database_cursor = database_connection.cursor()
    except Error as e:
        print(e)

def init_database():
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    database_cursor.execute("CREATE TABLE IF NOT EXISTS Movies(id int NOT NULL UNIQUE, year, title)")
    database_cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS movie_id_index ON Movies (id)")
    database_cursor.execute("CREATE TABLE IF NOT EXISTS Recommendations(id, recommendations)")
    close_connection()
  
def close_connection():
    global database_connection, database_cursor
    database_connection.close()
    database_connection = None
    database_cursor = None

def reset_database():
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    database_cursor.execute("DROP TABLE RecommendationS")
    database_cursor.execute("DROP TABLE Movies")
    

def insert_into_recomendations_table(recommendations):
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    database_cursor.executemany("INSERT INTO Recommendations VALUES (?, ?)", recommendations)
    database_connection.commit()
    close_connection()     
  
   
def insert_into_movies_table(movies):
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    database_cursor.executemany("INSERT INTO Movies VALUES (?, ?, ?)", movies)
    database_connection.commit()
    close_connection()


def get_all_movies():
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    response = database_cursor.execute("SELECT * FROM Movies").fetchall()
    close_connection()
    return response


  
def get_recommendation_for_movie_id(movie_id: int):
    if(database_connection is None or database_cursor is None):
        establish_db_connection()
    response = database_cursor.execute("SELECT * FROM Recommendations WHERE id = {0}".format(movie_id)).fetchall()
    close_connection()
    return response  

if __name__ == '__main__':
    """
    We create this to anable the usage of this file with python execution paramenters
    Usage:
    python -m data_prep.py prepare_data
    or:
    py.exe .\functions\data_prep.py prepare_data 
    """
    args = sys.argv
    if (len(args) <= 1):
        raise ValueError('No Parameters were set. No Function will be executed!')
    else:
        globals()[args[1]]()
