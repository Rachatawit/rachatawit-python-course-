print("1. THB to USD")
print("2. USD to THB")

choice = int(input("Choose choice(1 or 2)"))
amount = float(input("Enter Your Amount :"))

if choice == 1:
    result = amount / 35.5
    print(f"Calculate = {amount} / 35.5 = {result}")
    print("Result :",result)
elif choice == 2 :
    result = amount * 35.5
    print(f"Calculate = {amount} * 35.5 = {result}")
    print("Result :",result)
else :
    print("Invild Choice")