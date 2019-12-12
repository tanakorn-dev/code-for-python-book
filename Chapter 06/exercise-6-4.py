# จงรับชื่อเข้ามาทางแป้นพิมพ์ และแสดงผลทีละตัวอักษร
# จงรับนามสกุลเข้ามาทางแป้นพิมพ์ และแสดงผลทีละตัวอักษร โดยหากนามสกุลมีตัวอักษร "n" ไม่ต้องแสดงผล "n" ออกมา

firstname = input("Please enter firstname : ")
for x in firstname:
    print(x)

lastname = input("Please enter lastname : ")
for x in lastname:
    if x == "n":
        continue
    print(x)
