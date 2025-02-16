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

# Insert a record
mycursor.execute("""
INSERT INTO customer (name, address, salary)
VALUES ('Kavithma', 'Galle', 90000)
""")

# Commit the changes
mydb.commit()

print("Customer saved successfully...!")
