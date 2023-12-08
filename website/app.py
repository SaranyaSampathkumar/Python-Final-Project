# Import necessary modules from Flask
from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)
#Define location name and database
db_loc = 'database'
database_name = "Retail.db"
base_path = pathlib.Path().cwd()
#file_path = base_path / database_name
#file_path = db_loc /database_name

#renders the "index_fillin.html" template 
@app.route("/")
def index():
    return render_template("index_fillin.html")

#renders the "about.html" template #route for about page
@app.route("/about")
def about():
    return render_template("about.html")

#route for data page
@app.route("/data")
def data():
    try:

        #con = sqlite3.connect(db_locdatabase_name)
        # connect to the SQLite database
        con = sqlite3.connect('database/Retail.db')
        cur = con.cursor()
        #execute an SQL query to fetch all data from the "retails" table
        retails = cur.execute("SELECT * FROM retails").fetchall()
        #close the database connection
        con.close()
        return render_template("data.html", retails = retails) #variable = value
    except Exception as e:
        return f"Error: {str(e)}"

if __name__=="__main__":
    #run the flask application
     app.run(debug=True, port=5001)

