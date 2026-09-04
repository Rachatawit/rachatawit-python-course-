'''
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert Your text:")
letter = input("Character to find:")
for i in text:
    if i == letter:
        count += 1
print(f"{count} letters 'a' found in '{text}'")
'''

password = input("Insert Your Password:")
if len(password) >= 8 and '@' in password :
    print("Password Storng")
else :
    print("Password not Strong")

