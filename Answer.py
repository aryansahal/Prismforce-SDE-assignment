import json


def calculate_balance_sheet(input_data):
    expense_data = input_data['expenseData']
    revenue_data = input_data['revenueData']
    balance_sheet = {}

    for entry in revenue_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = timestamp.split('-')[1]

        if month not in balance_sheet:
            balance_sheet[month] = amount
        else:
            balance_sheet[month] += amount

    for entry in expense_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = timestamp.split('-')[1]

        if month not in balance_sheet:
            balance_sheet[month] = -amount
        else:
            balance_sheet[month] -= amount

    sorted_balance_sheet = sorted(balance_sheet.items(), key=lambda x: x[0])

    for month, balance in sorted_balance_sheet:
        print(f"Month: {month}, Balance: {balance}")


with open('1-input.json') as file:
    input_data = json.load(file)

calculate_balance_sheet(input_data)
