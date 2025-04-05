bill = float(input("Enter the bill amount: "))
tip = float(input("Enter tip percentage: "))

tip_amount = bill * (tip / 100)
total = bill + tip_amount

print(f"Tip: ${tip_amount}")
print(f"Total: ${total}")