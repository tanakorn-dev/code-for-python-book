# Boolean Operation `AND`

# ตารางการเปรียบเทียบแบบ AND
# | ค่าที่ 1 and ค่าที่ 2 | ผลลัพธ์ |
# | True  and True  | True  |
# | True  and False | False |
# | False and True  | False |
# | False and False | False |

a = True
b = True
print(a and b)

a = True
b = False
print(a and b)

a = False
b = True
print(a and b)

a = False
b = False
print(a and b)

# จงเเขียนโปรแกรมเพื่อตรวจสอบว่า ค่า x มากกว่า ค่า y และน้อยกว่าค่า z หรือไม่
x = 30
y = 10
z = 15

print((x > y) and (x < z))