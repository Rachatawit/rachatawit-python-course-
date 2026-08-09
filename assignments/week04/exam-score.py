scores = []
for i in range(5):
    scores.append(int(input("คะแนน: ")))
for score in scores:
    if score >= 50:
        print("ผ่าน")
    else:
        print("ไม่ผ่าน")