prices = []
for i in range(6):
    prices.append(int(input("ราคา: ")))
budget = int(input("งบประมาณ: "))
total = 0
buy = []
for price in prices:
    if total + price <= budget:
        print("buy")
        total += price
        buy.append(price)
    else:
        print("cannot buy")

print("ซื้อได้:", buy)
print("ใช้ไป:", total)
print("เหลือ:", budget - total)