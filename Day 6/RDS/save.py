import mysql.connector

mydb = mysql.connector.connect(
    host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="12345678",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE ijse")

# Insert a record
mycursor.execute("""
INSERT INTO customer (name, address, salary)
VALUES ('Kavithma', 'Galle', 90000)
""")

# Commit the changes
mydb.commit()

print("Customer saved successfully...!")
