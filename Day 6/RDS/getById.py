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


# Get a record by id
def get_customer_by_id(customer_id):
    mycursor.execute("SELECT * FROM customer WHERE id = %s", (customer_id,))
    customer = mycursor.fetchone()

    if customer:
        print(customer)
    else:
        print("Customer not found...!")


get_customer_by_id(1)
