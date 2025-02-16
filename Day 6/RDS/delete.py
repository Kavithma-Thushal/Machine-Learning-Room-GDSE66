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

# Delete a record by id
mycursor.execute("""
DELETE FROM customer
WHERE id = 2
""")

# Commit the changes
mydb.commit()

print("Customer deleted successfully...!")
