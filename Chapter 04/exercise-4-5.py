# จงเขียนโปรแกรมรับอายุของนักเรียน และทำจามคำสั่งต่อไปนี้

# ตรวจสอบว่าอายุนักเรียนมากกว่า 18 หรือไม่
# ถ้า a = 13, b = 20 จงหาว่าอายุของนักเรียน อยู่่ในช่วง a และ b หรือไม่
# ถ้า x = 15, y = 25 จงหาว่าอายุของนักเรียน เท่ากับ x หรือ y หรือไม่

age_str = input("Please enter your age : ")
age = int(age_str)
print(age)

print(age > 18)

a = 13
b = 20
print((age >= a) and (age <= b))

x = 15
y = 25
print((age == x) or (age == y))
