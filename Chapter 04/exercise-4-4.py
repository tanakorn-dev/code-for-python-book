# Boolean Operation `OR`

# ตารางการเปรียบเทียบแบบ OR
# | ค่าที่ 1 or ค่าที่ 2 | ผลลัพธ์ |
# | True  or True  | True  |
# | True  or False | True  |
# | False or True  | True  |
# | False or False | False |

a = True
b = True
print(a or b)

a = True
b = False
print(a or b)

a = False
b = True
print(a or b)

a = False
b = False
print(a or b)

# จงเเขียนโปรแกรมเพื่อตรวจสอบว่า ค่า x มากกว่า ค่า y หรือน้อยกว่าค่า z หรือไม่
x = 30
y = 10
z = 15

print((x > y) and (x < z))