# Address Book:
# I Build a simple address book application that allows users to store 
# contact information (name, phone number, email, etc.)
# and perform operations like adding new contacts, searching for contacts,
# and deleting contacts.

import csv
import os
import pandas as pd

file_name="data.csv"
headers = ['Name', 'Phone', 'Email']

if not os.path.exists(file_name):
    with open(file_name,mode='w',newline="")as file:
        writer=csv.writer(file)
        writer.writerow(headers)
 

class CSV:
    
    def adddata(file_name,data):
        with open(file_name, mode='a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow(data) 
            
 
   
        print(f"Data appended to '{file_name}' successfully.")
        
        
    def search_contact(file_name, target_name):
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == target_name:
                    return row
        return None
 
def add_entry(file_name, value):
    """
    Fetch a row from the CSV file where the 'Name' column matches the given value.
    """
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            if 'Name' not in reader.fieldnames:
                raise ValueError("Header 'Name' not found in CSV file.")
            for row in reader:
                if row['Name'].strip() == value.strip():
                    return row
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except ValueError as e:
        print(e)
    return None

def delete_entry    (value_to_delete):
    df = pd.read_csv(file_name)
    filtered_df = df[df['Name'] != value_to_delete]
    filtered_df.to_csv(file_name, index=False)
    print("deleted")

def main():
    """
    Main function to interact with the address book.
    """
    while True:
        print("""
        Press 1 to add a new entry
        Press 2 to check an entry
        Press 3 to delete an entry
        Press 0 to exit
        """)
        
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            data = [name, phone, email]
            CSV.adddata(file_name, data)
            
        elif choice == 2:
            value = input("Type the name of the row you want to check: ")
            result = add_entry
            (file_name, value)
            if result:
                print()
                print(f"name: {result['Name']}")
                print(f"phone: {result['Phone']}")
                print(f"email: {result['Email']}")
            else:
                print("No matching row found.")
            
        elif choice == 3:
            value_to_delete = input("Enter the name of the row you want to delete: ")
            delete_entry(value_to_delete)
            
        elif choice == 0:
            print("Exiting...")
            break
        
        else:
            print("Incorrect value. Select an option from the menu.")

 
main()
