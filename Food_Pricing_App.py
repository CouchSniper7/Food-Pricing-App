# Pricing App charges by the weight of the food eaten

# constants
tax = 7.25 # tax rate in percentage

# Welcome message
print("Welcome to the food court.")

# Prompt for user Name
name = (input("Please enter your name: "))

#Prompt for user pounds of food
weight = float(input("Please enter the weight of food in pounds: "))

#Pricing groups
if 0 <= weight <= 2:
    price = 16.99
elif 2 < weight <= 3.7:
    price = 21.99
elif 3.7 < weight <= 4.4:
    price = 28.75
elif weight > 4.4:
    price = 34.99

# compute total price
subtotal = price
taxdue = (tax / 100) * price
totalprice = subtotal + taxdue

# Display output to user
print(f"Customer Name: {name}")
print(f"Pounds eaten: {weight:.2f}") # :.2f shows 2 decimal places
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax: {taxdue:.2f}")
print(f"Total amoiunt due: {totalprice:.2f}")

# Goodbye message
print("Thank you for visiting. Please come again!")
