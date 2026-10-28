# Tuple-Based Product Catalogue Audit

products = [
    ("P101", 500.0, 10),
    ("P102", 1200.0, 3),
    ("P103", 0.0, 5),
    ("P104", 750.0, -2),
    ("P105", 300.0, 2)
]

reorder_level = 5
total_inventory_value = 0

print("PRODUCT CATALOGUE AUDIT")
print("-" * 50)

for product in products:
    product_id, price, stock = product

    # Validate product records
    if price <= 0 or stock < 0:
        print("Invalid record:", product)
        continue

    # Calculate inventory value
    value = price * stock
    total_inventory_value += value

    print("Product ID:", product_id)
    print("Price: Rs.", price)
    print("Stock:", stock)
    print("Inventory value: Rs.", value)

    # Check replenishment requirement
    if stock <= reorder_level:
        print("Status: Replenishment Required")
    else:
        print("Status: Stock Sufficient")

    print("-" * 50)

print("Total Inventory Value: Rs.",
      total_inventory_value)