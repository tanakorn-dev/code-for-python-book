# การใช้ Boolean Operation ใน If

# AND
a = 300
b = 43
c = 600

# เขียนโปรแกรมตรวจสอบว่า ถ้า a มากกว่า b และ c มากกว่า a ให้แสดงคำว่า "เงื่อนไขทั้งสองเป็นจริง"
if a > b and c > a:
  print("เงื่อนไขทั้งสองเป็นจริง")

# OR
# เขียนโปรแกรมตรวจสอบว่า ถ้า a มากกว่า b หรือ a มากกว่า c ให้แสดงคำว่า "เงื่อนไขหนึ่งในนั้นเป็นจริง"
if a > b or a > c:
  print("เงื่อนไขหนึ่งในนั้นเป็นจริง")