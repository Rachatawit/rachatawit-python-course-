# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่คัว (a, e ,i ,o ,u)

name = input("Enter Your Name :")
vowel = "a,e,i,o,u,A,E,I,O,U"
count = 0
for letter in name:
    if letter in vowel:
        count = count + 1
print("จำนวนสระทั้งหมด" ,count,"ตัว")
