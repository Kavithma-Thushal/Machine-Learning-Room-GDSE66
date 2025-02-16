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

# Check if the table exists
mycursor.execute("SHOW TABLES LIKE 'customer'")
table_exists = mycursor.fetchone()

if table_exists:
    print("Table already exists...!")
else:
    # Create the table
    mycursor.execute("""
    CREATE TABLE customer (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255),
        salary DECIMAL(10, 2)
    )
    """)

    # Commit the changes
    mydb.commit()

    print("Table created successfully...!")
