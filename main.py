import os
import sys
from database_setup import MariaDBManager

def main():
    db_user = input("Enter MariaDB username: ")
    db_password = input("Enter MariaDB password: ")
    db_host = input("Enter MariaDB host: ")
    db_port = input("Enter MariaDB port: ")

    db_manager = MariaDBManager(db_user, db_password, db_host, db_port)

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Welcome to the MariaDB CRUD application!\n")
        print("Please select from the following options: ")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Data")
        print("4. Select Data")
        print("5. Update Data")
        print("6. Delete Data")
        print("7. Drop Table")
        print("8. Drop Database")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dbname = input("Enter the name of the database to create: ")
            db_manager.create_database(dbname)
        elif choice == '2':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table to create: ")
            db_manager.create_table(table_name)
        elif choice == '3':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table: ")
            name = input("Enter the name: ")
            age = int(input("Enter the age: "))
            db_manager.insert_data(table_name, name, age)
        elif choice == '4':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table: ")
            db_manager.select_data(table_name)
        elif choice == '5':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table: ")
            record_id = int(input("Enter the ID of the record to update: "))
            name = input("Enter the new name (leave blank to skip): ")
            age = input("Enter the new age (leave blank to skip): ")
            age = int(age) if age else None
            db_manager.update_data(table_name, record_id, name, age)
        elif choice == '6':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table: ")
            record_id = int(input("Enter the ID of the record to delete: "))
            db_manager.delete_data(table_name, record_id)
        elif choice == '7':
            dbname = input("Enter the name of the database: ")
            db_manager.db_name = dbname
            table_name = input("Enter the name of the table to drop: ")
            db_manager.drop_table(table_name)
        elif choice == '8':
            dbname = input("Enter the name of the database to drop: ")
            db_manager.drop_database(dbname)
        elif choice == '9':
            print("Thank you for using the MariaDB CRUD application!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
