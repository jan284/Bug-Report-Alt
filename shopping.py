#!/usr/bin/env python3
# shopping.py

# Create list of initial item prices
price_list = [10.11, 7.99, 5.99, 2.49, 0.99]

# Initialize variable to store tax multiplier
tax_rate = 1.06

# Define function that will take a list of int and an int as arguments
def add_tax(prices, tax):
    # Iterate through list of prices
    for price in prices:
        # Calculate price after tax
        price *= tax
        # Round final price to 2 dp and print
        print(round(price, 2))

# Call add_tax func 
add_tax(price_list, tax_rate)
