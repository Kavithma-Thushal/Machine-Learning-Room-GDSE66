import mysql.connector

mydb = mysql.connector.connect(
    host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="12345678",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE ijse")

# Delete a record by id
mycursor.execute("""
DELETE FROM customer
WHERE id = 2
""")

# Commit the changes
mydb.commit()

print("Customer deleted successfully...!")
