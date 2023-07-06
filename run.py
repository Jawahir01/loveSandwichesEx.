import gspread
from google.oauth2.service_account import Credentials

#Scope is constantant so we write it in CAP
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

"""
Check if our data is working 
sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data)
"""

def get_sales_data():
    """
Get sales figures input from the user
    """
    print('\n(+)Please enter sales data from th last markets.')
    print('(+)Data should be six numbers, separated by commas.')
    print('(+)Example: 11,12,13,14,15,16\n')

    data_str = input('(+)Enter your data here: ')
    sales_data = data_str.split(",")
    #print(f'(+)The data provided is {sales_data}')
    validate_data(sales_data)


def validate_data(values):
    """
    Validate our data given from the user before allowing the rest of the
    program to run:
    converts all string values into integers, raise ValueError if string cannot
    be converted or if there aren't exactly 6 values
    """
    [int(value) for value in values]
    try:
        if len(values) != 6:
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")


get_sales_data()