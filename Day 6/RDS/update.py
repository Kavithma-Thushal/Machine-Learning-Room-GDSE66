import mysql.connector

mydb = mysql.connector.connect(
    host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="12345678",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE ijse")

# Update a record by id
mycursor.execute("""
UPDATE customer
SET salary = 50000
WHERE id = 1
""")

# Commit the changes
mydb.commit()

print("Customer updated successfully...!")
