import mysql.connector
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE aws")


# Get all records from the customer table
def get_all_customers():
    mycursor.execute("SELECT * FROM customer")
    customers = mycursor.fetchall()

    if customers:
        print(customers)
    else:
        print("No customers found...!")


get_all_customers()
