print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()


sec = int(input("ใส่วินาที :"))
hours = sec // 3600
second_remain = sec % 3600
mi = second_remain // 60
second_remain = mi % 60

print(f"{sec} seconds = {hours} hour, {mi} minute, {second_remain}second")