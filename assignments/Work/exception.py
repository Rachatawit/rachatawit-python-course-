try:
    num1 = float(input("ตัวเลขที่ 1:"))
    num2 = float(input("ตัวเลขที่ 2:"))
    sig = input("เครื่องหมาย (+, -, *, /):")

    result = 0
    if sig == "+":
        result = num1 + num2
    elif sig == "-":
        result = num1 - num2
    elif sig == "*":
        result = num1 * num2
    elif sig == "/":
        result = num1 / num2
    else:
        raise ValueError("เครื่องหมายต้องเป็น + - * / เท่านั้น")
    
    print(f"{num1} {sig} {num2} = {result}")

except ValueError:
    print("กรอกข้อมูลที่เป็นตัวเลข")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
else:
    print("คำนวณเรียบร้อย")
finally :
    print("End")