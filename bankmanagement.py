import mysql.connector as mysql
from datetime import date

def db_connect():
    return mysql.connect(
        host="localhost",
        user="root",
        passwd="AR",
        database="Bank"
    )

def show_details(data):
    print("\n" + "="*80)
    print(" "*29 + "Your Bank Account Details")
    print("="*80)
    print(f"Account Number          : {data[0]}")
    print(f"User Name               : {data[1]}")
    print(f"Account Balance         : Rs. {data[3]}")
    print(f"Registered Mobile Number: {data[4]}")
    print(f"Nationality             : {data[5]}")
    print(f"E-Mail Address          : {data[6]}")
    print(f"Designation             : {data[7]}")
    print(f"Date of Birth           : {data[8]}")
    print("="*80 + "\n")

def open_account(cursor, db):
    uname = input("Enter Username: ")
    passwd = input("Enter Password: ")
    balance = int(input("Enter Opening Balance: "))
    mobile = input("Enter Mobile Number: ")
    nationality = input("Enter Nationality: ")
    email = input("Enter E-Mail: ")
    designation = input("Enter Designation: ")
    dob = input("Enter Your Date of Birth (YYYY-MM-DD): ")
    cursor.execute("SELECT MAX(Accountno) FROM details")
    last_acc = cursor.fetchone()[0] or 10000
    new_acc = last_acc + 7
    query = """
        INSERT INTO details (Accountno, Username, Password, Balance, Mobile, Nationality, Email, Designation, DOB) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.execute(query, (new_acc, uname, passwd, balance, mobile, nationality, email, designation, dob))
    db.commit()
    print(f"\n✅ Account Opened Successfully!\nYour Account Number is: {new_acc}")
    print("Opened on:", date.today())
    print("="*80 + "\n")

def account_details(cursor):
    acc = int(input("Enter Account Number: "))
    passwd = input("Enter Your Password: ")
    query = "SELECT * FROM details WHERE Accountno=%s AND Password=%s"
    cursor.execute(query, (acc, passwd))
    data = cursor.fetchone()
    if data:
        show_details(data)
    else:
        print("❌ Invalid Account Number or Password.")

def withdraw_money(cursor, db):
    acc = int(input("Enter Account Number: "))
    passwd = input("Enter Your Password: ")
    amount = int(input("Enter Withdrawal Amount: "))
    cursor.execute("SELECT * FROM details WHERE Accountno=%s AND Password=%s", (acc, passwd))
    data = cursor.fetchone()
    if not data:
        print("❌ Invalid Account Number or Password.")
        return
    if amount > data[3]:
        print("❌ Insufficient Balance!")
        return
    cursor.execute("UPDATE details SET Balance=Balance-%s WHERE Accountno=%s", (amount, acc))
    db.commit()
    print(f"\n✅ Withdrawal of Rs.{amount} completed on {date.today()}")
    show_details((acc, data[1], data[2], data[3]-amount, data[4], data[5], data[6], data[7], data[8]))

def deposit_money(cursor, db):
    acc = int(input("Enter Account Number: "))
    passwd = input("Enter Your Password: ")
    amount = int(input("Enter Deposit Amount: "))
    cursor.execute("SELECT * FROM details WHERE Accountno=%s AND Password=%s", (acc, passwd))
    data = cursor.fetchone()
    if not data:
        print("❌ Invalid Account Number or Password.")
        return
    if amount <= 0:
        print("❌ Invalid Deposit Amount.")
        return
    cursor.execute("UPDATE details SET Balance=Balance+%s WHERE Accountno=%s", (amount, acc))
    db.commit()
    print(f"\n✅ Deposit of Rs.{amount} completed on {date.today()}")
    show_details((acc, data[1], data[2], data[3]+amount, data[4], data[5], data[6], data[7], data[8]))

def account_statement(cursor):
    acc = int(input("Enter Account Number: "))
    cursor.execute("SELECT Accountno, Username, Balance FROM details WHERE Accountno=%s", (acc,))
    data = cursor.fetchone()
    if data:
        print("\n" + "="*80)
        print(" "*29 + "Your Account Statement")
        print("="*80)
        print(f"Account Number : {data[0]}")
        print(f"User Name      : {data[1]}")
        print(f"Balance        : Rs.{data[2]}")
        print("="*80 + "\n")
    else:
        print("❌ Account not found.")

def main():
    db = db_connect()
    cursor = db.cursor()
    print("="*80)
    print(" "*29 + "| BANK MANAGEMENT SYSTEM |")
    print("="*80)
    while True:
        print("\n1. OPEN NEW ACCOUNT")
        print("2. ACCOUNT DETAILS")
        print("3. MONEY WITHDRAWAL")
        print("4. MONEY DEPOSIT")
        print("5. ACCOUNT STATEMENT")
        print("6. EXIT")
        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("❌ Invalid input. Enter a number between 1-6.")
            continue
        if choice == 1:
            open_account(cursor, db)
        elif choice == 2:
            account_details(cursor)
        elif choice == 3:
            withdraw_money(cursor, db)
        elif choice == 4:
            deposit_money(cursor, db)
        elif choice == 5:
            account_statement(cursor)
        elif choice == 6:
            print("👋 Exiting... Thank you for using Bank Management System.")
            break
        else:
            print("❌ Invalid Choice. Please try again.")
    db.close()

if __name__ == "__main__":
    main()
