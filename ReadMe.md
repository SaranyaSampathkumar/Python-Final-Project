## Dataset Description:
The Sample Superstore dataset contains information about orders from a retail superstore.

## Data Collection: 
This contains the Sample Superstore dataset which we exported as csv file named retail_store.csv
      
## Website:

### app.py:
Flask application (app.py) defines a web server with three routes. The "/" route renders the "index_fillin.html" template, the "/about" route renders the "about.html" template, and the "/data" route connects to an SQLite database named "Retail.db" in the "database" folder. It executes an SQL query to fetch all data from the "retails" table and renders the "data.html" template passing the retrieved data to the template. 

To run app.py following code following command can be used: python .\website\app.py

## Templates:
Templates contains 3 html pages which is explained below:

### index_fillin.html: 
This HTML code displays Welcome message for "Sample - Superstore Dataset" and navigation links to the About and Data pages. 
      
### about.html: 
This displays information about the dataset, Each variable description and Link to the source of my dataset
      
### data.html: 
This html code displays 10 rows from Retail database.

## Database:

### checking.py:
It defines a function, create_db, which takes parameters for a SQLite database name, a CSV file containing retail_store data, and a table name retails. The function reads the CSV data and inserts it into a SQLite table. When executed, this script creates a SQLite database named "Retail.db" with a table named "retails," populated with data from the "retail_store.csv" file.
      
### Retail.db: 
This is the database which is created from checking.py which has data from our Sample Superstore dataset

## requirements.txt: 
This file contains all packages necessary to run your code. This file allow the user to install all necessary packages.
command used: pip install -r requirements.txt









