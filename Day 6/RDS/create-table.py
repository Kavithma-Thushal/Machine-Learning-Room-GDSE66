import mysql.connector

mydb = mysql.connector.connect(
    host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="12345678",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE ijse")

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
