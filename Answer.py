import json
from datetime import datetime
from collections import defaultdict


def calculate_balance_sheet(input_data):
    expense_data = input_data['expenseData']
    revenue_data = input_data['revenueData']
    month_list = []

    balance_sheet = defaultdict(int)

    for entry in revenue_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").month
        month_list.append(month)

        balance_sheet[month] += amount

    for entry in expense_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").month
        month_list.append(month)

        balance_sheet[month] -= amount
    month_list = list(dict.fromkeys(month_list))

    for month in range(1, max(month_list)+1):
        balance = balance_sheet[month]
        print(f"Month: {month:02d}, Balance: {balance}")


with open('1-input.json') as file:
    input_data = json.load(file)

calculate_balance_sheet(input_data)
