"""
Gspread import imports the entire gspread libriray so we can have access any function, class and object in it
"""

import gspread

"""
and this import importes the credentials class
"""

from google.oauth2.service_account import Credentials

"""
The scope IAM stands for Identity and Access Management. This configuration specifies what the user has access to.
The scope lists the APIs that the  program should access in order to run.
"""
#In python constant variable names must be UPPERCASE
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

def get_sales_data():
    """
    Get sales figures input from the user
    """
    while True: 
        print("Please enter sales data from the last market.")
        print("Data should be six numbers, sebarated by commas.")
        print("Example: 10,20,30,40,50,60\n")
        data_str = input("Please insert the sales data: ")
        print(f"The data provided is {data_str}")
        
        sales_data = data_str.split(",")
        

        if validate_data(sales_data):
            print("Data is valid!\n")
            break
    return sales_data()

def validate_data(values):
    """
    Test if the data that provided is exactly 6 numbers and
    """
    
    try:
        [int(num) for num in values]
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided.
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated succesfully...\n")

        
#def main():
    """
    Calls all the functions
    """
data = get_sales_data()
sales_data = [int(num) for num in data]

#print("Welcome to Love Sandwich")
#main()