'''
apple = input("Enter a number: ")
try:
    x = int(apple) - 10
    print(f"Result: {x}")
except ValueError:
    print("Please enter a valid number!")
'''

'''
print("\n=== STRING INDEXING ===")
fruit = 'banana' 'apple'
print(f"fruit = {fruit}")
print(f"fruit[1] = {fruit[8]}")  # 'a'
'''

'''
print("\n=== TRAVERSING STRINGS ===")
message = "hello"
index = 0

print("Method 1: Using for loop with enumerate")
for i, char in enumerate(message): #งง
    print(f"message[{i}] = {char}")
'''

'''
print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  # True
print("'at' not in 'battle':", 'at' not in 'battle')  # False
'''

print("\n=== STRING METHODS ===")
text = "welcome to the world of python"

# Case methods
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'welcome': {text.startswith('welcome')}")
print(f"Ends with 'python': {text.endswith('python')}")