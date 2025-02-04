# Eliya Statema
# 2/3/25
# Shipping Charges

weight = float(input("Enter the weight of the package: "))

if weight <= 2:
    shipping_cost = 1.50
elif weight > 2 and weight <= 6:
    shipping_cost = 3.00
elif weight > 6 and weight <= 10:
    shipping_cost = 4.00
elif weight > 10:
    shipping_cost = 4.75
print(f"Shipping charge: ${shipping_cost:.2f}")