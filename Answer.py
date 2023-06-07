import json


def calculate_balance_sheet(input_data):
    expense_data = input_data['expenseData']
    revenue_data = input_data['revenueData']

    # Create a dictionary to store the balances for each month
    balance_sheet = {}

    # Iterate over the revenue entries and calculate the balance for each month
    for entry in revenue_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = timestamp.split('-')[1]  # Extract the month from the timestamp

        if month not in balance_sheet:
            balance_sheet[month] = amount
        else:
            balance_sheet[month] += amount

    # Iterate over the expense entries and subtract the expense amount from the corresponding month's balance
    for entry in expense_data:
        timestamp = entry.get('startDate')
        amount = entry.get('amount', 0)
        month = timestamp.split('-')[1]  # Extract the month from the timestamp

        if month not in balance_sheet:
            balance_sheet[month] = -amount
        else:
            balance_sheet[month] -= amount

    # Sort the balance sheet by month
    sorted_balance_sheet = sorted(balance_sheet.items(), key=lambda x: x[0])

    # Print the balance sheet
    for month, balance in sorted_balance_sheet:
        print(f"Month: {month}, Balance: {balance}")


# Read the input data from a JSON file
with open('2-input.json') as file:
    input_data = json.load(file)

# Calculate and print the balance sheet
calculate_balance_sheet(input_data)
