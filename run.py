import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

    while True:
        print('\n(+)Please enter sales data from th last markets.')
        print('(+)Data should be six numbers, separated by commas.')
        print('(+)Example: 11,12,13,14,15,16\n')

        data_str = input('(+)Enter your data here: ')
        sales_data = data_str.split(",")

    
        #print(f'(+)The data provided is {sales_data}')
    
        if validate_data(sales_data):
            print('Data is Valid!\n')
            break

    return sales_data



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
        return False

    return True

"""
def update_sales_worksheet(data):
  
    #update sales worksheet, add new row with the list data provided
  
    print("Updating sales worksheet... \n")
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully..\n")

def update_surplus_worksheet(data):
 
    #update surplus worksheet, add new row with the surplus data calculated

    print("Updating sales worksheet... \n")
    surplus_worksheet = SHEET.worksheet('surplus')
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully..\n")

"""

def update_worksheet(data, worksheet):
    """
    - Receive a list of integers to be inserted to the worksheet
    - Update the relevent worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_surplus_data(sale_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    -Positive surplus indicates waste
    - Negative surlpus indicates extra made when stock was sold out
    """
    print("Calculating surplus data... \n")
    stock = SHEET.worksheet('stock').get_all_values()
    #pprint(stock)
    stock_row = stock[-1]
    #print(f'Stock row: {stock_row}')
    #print(f'Sales row: {sale_row}')

    surplus_data=[]
    for stock, sales in zip(stock_row, sale_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)

    return surplus_data


def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwish and return the data
    as a list of lists.
    """
    sales = SHEET.worksheet('sales')
    #column = sales.col_values(3)  we can get a single column by a number inside col_value method
    # print(column)
    columns = []
    for ind in range(1, 7):
        column = sales.col_values(ind)
        columns.append(column[-5:])
    return columns


def calculate_sales_data(data):
    """
    Calculate the average stock for each item type, adding 10%
    """
    print("Calculating the stck data...\n")
    new_stock_data= []
    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column) #It should be 5
        stcok_num = average * 1.1
        new_stock_data.append(round(stcok_num))

    return new_stock_data


def main():
    """
    Run All program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'sales')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'surplus')
    sales_columns = get_last_5_entries_sales()
    stock_data = calculate_sales_data(sales_columns)
    update_worksheet(stock_data, 'stock')
print("\n Welcome to Love Sandwiches Data Automation")
main()

