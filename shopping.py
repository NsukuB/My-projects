# Request user to input three different names of products
product1 = input("Please enter the name of the first product: ")
product2 = input("Please enter the name of the second product: ")
product3 = input("Please enter the name of the third product: ")

# Request for the price of each product with two decimal values
price1 = float(input(f"Please enter the price of {product1}: "))
price2 = float(input(f"Please enter the price of {product2}: "))
price3 = float(input(f"Please enter the price of {product3}: "))

# Calculate the total sum of all three products
total_sum = price1 + price2 + price3

# Calculate the average price of the three products
average_price = total_sum / 3

# Print out the results
print(f"The Total of {product1}, {product2}, {product3} is R{total_sum:.2f} and the average price of the items is R{average_price:.2f}.")
