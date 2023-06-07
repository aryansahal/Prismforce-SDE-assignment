from ctypes import sizeof
import json
from datetime import datetime
from collections import defaultdict


def calculate_balance_sheet(input_data):
    expense_data = input_data['expenseData']
    revenue_data = input_data['revenueData']
    month_list = []

    # Create a dictionary to store the balances for each month
    balance_sheet = defaultdict(int)

    # Calculate the balance for each revenue entry
    for entry in revenue_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").month
        month_list.append(month)

        balance_sheet[month] += amount

    # Calculate the balance for each expense entry
    for entry in expense_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").month
        month_list.append(month)

        balance_sheet[month] -= amount
    month_list = list(dict.fromkeys(month_list))

    # Print the balance sheet
    for month in range(1, max(month_list)+1):
        balance = balance_sheet[month]
        print(f"Month: {month:02d}, Balance: {balance}")


# Read the input data from a JSON file
with open('1-input.json') as file:
    input_data = json.load(file)

# Calculate and print the balance sheet
calculate_balance_sheet(input_data)
