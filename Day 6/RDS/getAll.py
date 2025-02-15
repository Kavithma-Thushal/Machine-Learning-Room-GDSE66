import mysql.connector


def getAll():
    mydb = mysql.connector.connect(
        host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="12345678",
    )

    mycursor = mydb.cursor()

    # Use the database
    mycursor.execute("USE ijse")

    # Get all records from the customer table
    mycursor.execute("""
    SELECT * FROM customer
    """)

    # Fetch all results
    results = mycursor.fetchall()

    # Check if records exist and return
    if results:
        return results
    else:
        return "No customers found."


# Example usage
customers = getAll()
print(customers)
