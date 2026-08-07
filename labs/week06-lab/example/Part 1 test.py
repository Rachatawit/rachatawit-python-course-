def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    
"""
print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()
"""


def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium == True :
        premium = ("Premium_user")
    else :
        premium = ("Standard_user")
    return f"{username} (age : {age}) - {premium}"
print(create_user_profile("Rachatawit",99))
print(create_user_profile("Jew"))
print(create_user_profile("JJ" , 23 , True))