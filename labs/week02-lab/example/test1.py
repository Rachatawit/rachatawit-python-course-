print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

# input
area = float(input("ใส่รัศมี :"))

# process
calculate = 3.14159 * area ** 2
circumference = 2 * 3.14159 * area

#output
print(calculate)
print(circumference)