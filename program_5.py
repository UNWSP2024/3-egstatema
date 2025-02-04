# Eliya Statema
# 2/3/25
# Hot Dog Order

tax_rate = 0.07

print('''MENU:
Hot Dog ($3.50)
Chili Dog ($4.50)
Cheese ($0.50)
Peppers ($0.75)
Grilled Onions ($1.00)
''')

hot_dog_type = input("What kind of hot dog would you like? ")
if hot_dog_type == 'Hot dog':
    hot_dog_price = 3.50
elif hot_dog_type == 'Chili dog':
    hot_dog_price = 4.50

topping_choice = input("Would you like toppings? ")
if topping_choice == 'Yes':
    topping = input("What topping would you like? ")
    if topping == 'Cheese':
       topping_price = 0.50
    elif topping == 'Peppers':
       topping_price = 0.70
    elif topping == 'Grilled onions':
       topping_price = 1.00
elif topping_choice == 'No':
    topping_price = 0

subtotal = hot_dog_price + topping_price
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print(f'''
SUBTOTAL: ${subtotal:.2f}
SALES TAX: ${sales_tax:.2f}
*** TOTAL: ${total:.2f} ***''')