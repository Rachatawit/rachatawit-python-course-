def THB_to_USD(THB):
    """Converts THB to USD"""
    USD = THB / 32
    return USD

def USD_to_THB(USD):
    """Converts USD to THB"""
    THB = USD * 32
    return THB

def convert(con, amount):
    """Converts Currency"""
    if con.upper() == "USD":
        converted = THB_to_USD(amount)
        return f"{amount} THB = {converted:.2f} USD"
    elif con.upper() == "THB":
        converted = USD_to_THB(amount)
        return f"{amount} USD = {converted:.2f} THB"
    else:
        return "Invalid currency. Use 'USD' or 'THB"

print("Currency Converter:")
print(convert("usd", 3000))
print(convert("thb", 235))
print()


'''
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person(5)
greet_person("Bob")
greet_person("Charlie")
print()
'''

'''
def introduce_person(name, age, city):
    """Introduces a person with their details"""
    print("fHi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")
'''

'''
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(9, 3)
calculate_rectangle_area(10, 5)
'''

'''
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()
'''

