def deposit():
    balance = 1000
    print(f"ยอดเงินเริ่มต้น: {balance} บาท")
    try:
        money = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
    else:
        balance = balance + amount
        print(f"\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
deposit()