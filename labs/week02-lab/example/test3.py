# Shopping Calculator Template
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# : Calculate subtotal ราคาเต็มเท่าไหร่
subtotal = item_price * quantity
# : Calculate discount amount ได้ส่วนลด
discount = subtotal * (discount_percent / 100)
# : Calculate price after discount ราคาหลังลดแล้ว
price = subtotal - discount
# : Calculate tax amount ภาษีเท่าไหร่
tax = price * (tax_percent / 100)
# : Calculate final total สรุปต้องจ่ายเท่าไหร้
total = price + tax
# : Display itemized receipt พ่นออกมาทางหน้าจอ
print("Subtotal :",subtotal)
print("Discount Amount :",discount)
print("Price :",price)
print("tax amount :",tax)
print("Final total :",total)
