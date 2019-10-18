name_list = ['Somchai', 'Panee' , 'Surat', 'Manee']
point_list = [9, 7, 9, 8]

# จงแสดงผลข้อมูลของ list ตั้งแต่ลำดับที่ 2 เป็นต้นไป ทั้ง 2 list
print(name_list[1:]) # Respond: ['Panee', 'Surat', 'Manee']
print(point_list[1:]) # Respond: [7, 9, 8]

# จงแสดงจำนวนนับตัวอักษรของชื่อในลำดับที่ 2 ของ list name_list
print(len(name_list[1])) # Respond: 5

# จงแสดงค่าใน name_list และ point_list คู่กัน โดยคั่นด้วยช่องว่าง ตัวอย่าง 'Somchai 9'
print(name_list[0],point_list[0]) # Respond: Somchai 9
print(name_list[1],point_list[1]) # Respond: Panee 7
print(name_list[2],point_list[2]) # Respond: Surat 9
print(name_list[3],point_list[3]) # Respond: Manee 8

# จงบวกข้อมูลใน point_list ลำดับที่ 1 และ 2
print(point_list[0] + point_list[1]) # Respond: 16

# จงลบข้อมูลใน point_list ลำดับที่ 1 และ 4
print(point_list[0] - point_list[3]) # Respond: 1

# จงคูณข้อมูลใน point_list ลำดับที่ 2 และ 3
print(point_list[1] * point_list[2]) # Respond: 63

# จงหารข้อมูลใน point_list ลำดับที่ 1 และ 3
print(point_list[0] / point_list[2]) # Respond: 1.0