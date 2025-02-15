import mysql.connector


def getById(customer_id):
    mydb = mysql.connector.connect(
        host="database-1.c1e684cqc92y.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="12345678",
    )

    mycursor = mydb.cursor()

    # Use the database
    mycursor.execute("USE ijse")

    # Get the record by id
    mycursor.execute("""
    SELECT * FROM customer
    WHERE id = %s
    """, (customer_id,))

    # Fetch the result
    result = mycursor.fetchone()

    # Check if record exists and return
    if result:
        return result
    else:
        return "No customer found with the given id."


# Example usage
customer = getById(1)
print(customer)
