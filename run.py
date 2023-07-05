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

    data_str = int(input('(+)Enter your data here: '))
    print(f'(+)The data provided is {data_str}')

get_sales_data()