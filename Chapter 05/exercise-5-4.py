# จงรับคะแนนเข้ามาทางแป้นพิมพ์ และแสดงผลเกรดทางหน้าจอ โดยมีเงื่อนไขดังต่อไปนี้
# ถ้าคะแนน น้อยกว่า 50 แสดงผล "เกรด F"
# ถ้าคะแนน มากกว่าหรือเท่ากับ 50 และ น้อยกว่า 60 แสดงผล "เกรด D"
# ถ้าคะแนน มากกว่าหรือเท่ากับ 60 และ น้อยกว่า 70 แสดงผล "เกรด C"
# ถ้าคะแนน มากกว่าหรือเท่ากับ 70 และ น้อยกว่า 80 แสดงผล "เกรด B"
# ถ้าคะแนน มากกว่า 80 แสดงผล "เกรด A"

score = int(input("Please enter score : "))

if score < 50:
    print("เกรด F")
elif score >= 50 and score < 60
    print("เกรด D")
elif score >= 60 and score < 70
    print("เกรด C")
elif score >= 70 and score < 80
    print("เกรด B")
else:
    print("เกรด A")
