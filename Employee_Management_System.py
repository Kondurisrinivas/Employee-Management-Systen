# importing mysql connector
import mysql.connector

# making Connection
con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="emp"
) 

# Function to Add Dummy Data to empd table
def Add_Dummy_Data():
    dummy_data = [
        ('John Doe', 'Manager', 50000),
        ('Jane Smith', 'Developer', 40000),
        ('Bob Johnson', 'Analyst', 45000),
        ('Alice Williams', 'Designer', 38000),
        ('Charlie Brown', 'Tester', 42000),
        ('Eva Davis', 'Administrator', 48000),
        ('Frank Wilson', 'Engineer', 55000),
        ('Grace Miller', 'Coordinator', 36000),
        ('Henry Taylor', 'Supervisor', 51000),
        ('Ivy Jackson', 'Programmer', 43000),
        ('David Lee', 'Consultant', 60000),
        ('Sophie Turner', 'Data Scientist', 58000),
        ('Michael Chen', 'Security Analyst', 47000),
        ('Olivia Robinson', 'HR Specialist', 42000),
        ('William Garcia', 'Business Analyst', 49000),
    ]

    # Inserting Dummy Data into the Employee Table
    sql = 'INSERT INTO empd (name, post, salary) VALUES (%s, %s, %s)'
    c = con.cursor()

    # Executing the SQL Query for each dummy data entry
    c.executemany(sql, dummy_data)

    # commit() method to make changes in the table
    con.commit()
    print("Dummy Data Added Successfully!!!")
    menu()

def Search_Employee():
    Id = int(input("Enter Employee Id to search: "))

    # Query to Select Employee by ID
    sql = 'SELECT * FROM empd WHERE id=%s'
    data = (Id,)
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql, data)

    # Fetching Employee details
    result = c.fetchone()
    
    if result is not None:
        print("Employee Found:")
        print("__________________________________________________")
        print("Employee Id:", result[0])
        print("Employee Name:", result[1])
        print("Employee Post:", result[2])
        print("Employee Salary:", result[3])
        print("___________________________________________________")

    else:
        print("Employee not found.")
    menu()

# Function to Add Employee
def Add_Employ():
    # Omitting ID input as it's auto-incremented
    Name = input("Enter Employee Name : ")
    Post = input("Enter Employee Post : ")
    Salary = input("Enter Employee Salary : ")
    data = (Name, Post, Salary)

    # Inserting Employee details in the Employee Table
    sql = 'INSERT INTO empd (name, post, salary) VALUES (%s, %s, %s)'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql, data)

    # commit() method to make changes in the table
    con.commit()
    print("Employee Added Successfully!!!")
    menu()

# Function to Promote Employee
def Promote_Employee():
    Id = int(input("Enter Employee's Id :"))

    # Checking if Employee with given Id Exists or Not
    if not check_employee(Id):
        print("Employee does not exist\nTry Again\n")
        menu()
    else:
        Amount = int(input("Enter increase in Salary :"))

        # Query to Fetch Salary of Employee with given Id
        sql = 'SELECT salary FROM empd WHERE id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # Fetching Salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount

        # Query to Update Salary of Employee with given Id
        sql = 'UPDATE empd SET salary=%s WHERE id=%s'
        d = (t, Id)

        # Executing the SQL Query
        c.execute(sql, d)

        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        menu()

# Function to Remove Employee with given Id
def Remove_Employ():
    Id = int(input("Enter Employee Id : "))

    # Checking if Employee with given Id Exists or Not
    if not check_employee(Id):
        print("Employee does not exist\nTry Again\n")
        menu()
    else:

        # Query to Delete Employee from Table
        sql = 'DELETE FROM empd WHERE id=%s'
        data = (Id,)
        c = con.cursor()

        # Executing the SQL Query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Employee Removed")
        menu()


# Function To Check if Employee with
# given Id Exists or Not
def check_employee(employee_id):
    # Query to select all Rows from employee Table
    sql = 'SELECT * FROM empd WHERE id=%s'

    # Creating a cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Executing the SQL Query
    c.execute(sql, data)

    # Fetching one row from the result
    result = c.fetchone()

    # Checking if the result is not None
    if result is not None:
        return True
    else:
        return False

# Function to Display All Employees
# from Employee Table
def Display_Employees():
    # query to select all rows from the Employee Table
    sql = 'SELECT * FROM empd'
    c = con.cursor()

    # Executing the SQL Query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id : ", i[0])
        print("Employee Name : ", i[1])
        print("Employee Post : ", i[2])
        print("Employee Salary : ", i[3])
        print("----------------------------------------------------------------------")

    menu()

# menu function to display menu
def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("0 to Search for an Employee")
    print("1 to Add Employee")
    print("2 to Remove Employee ")
    print("3 to Promote Employee")
    print("4 to Display Employees")
    print("5 to Add Dummy Data!!")
    print("6 to Exit")
    

    ch = int(input("Enter your Choice:"))
    print("----------------------------------------------------------------------------------------------------")
    if ch==0:
        Search_Employee()
    elif ch == 1:
        Add_Employ()
    elif ch == 2:
        Remove_Employ()
    elif ch == 3:
        Promote_Employee()
    elif ch == 4:
        Display_Employees()
    elif ch == 5:
        Add_Dummy_Data()
    elif ch == 6:
        exit(0)
    else:
        print("Invalid Choice")
        menu()

# Calling menu function
menu()
l=[1,2,3,45,]
b=[i for i in l if i%2!=0]
a=lambda x:x*2