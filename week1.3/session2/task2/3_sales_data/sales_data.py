# Week 1.3, Session 2: Sales Data Statistics

import csv
from pathlib import Path

sales_file = Path(__file__).with_name("sales.csv")

largest_sale = {"date": "", "amount": 0}
average_total = 0
row_count = 0
widget_totals = {}

try:
    with sales_file.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) < 5:
                continue

            date, product, sales_amount, units_sold, region = row
            sales_amount = int(sales_amount)
            units_sold = int(units_sold)

            row_count += 1
            average_total += sales_amount

            if sales_amount > largest_sale["amount"]:
                largest_sale = {"date": date, "amount": sales_amount}

            widget_totals[product] = widget_totals.get(product, 0) + units_sold

    average_sale = average_total / row_count
    best_widget = max(widget_totals, key=widget_totals.get)

    print(f"Largest sale day: {largest_sale['date']} with £{largest_sale['amount']}")
    print(f"Average sale amount: £{average_sale:.2f}")
    print(f"Best-selling widget: {best_widget} ({widget_totals[best_widget]} units)")

except FileNotFoundError:
    print(f"Could not find {sales_file.name}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget

# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows