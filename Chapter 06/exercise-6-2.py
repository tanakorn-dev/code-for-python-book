# The break Statement
# จากลิสสัตว์ต่างๆ จงแสดงข้อมูลออกมาทีละข้อมูล โดยใช้ For Loop แต่หากแสดงคำว่า "dog" ให้หยุดแสดงผล
animals = ["elephant", "tiger", "penguin", "bird", "dog", "cat"]
for x in animals:
  print(x) 
  if x == "dog":
    break

# The continue Statement
# จากลิสสัตว์ต่างๆ จงแสดงข้อมูลออกมาทีละข้อมูล โดยใช้ For Loop โดยไม่แสดงคำว่า "dog" ออกมา
animals = ["elephant", "tiger", "penguin", "bird", "dog", "cat"]
for x in animals:
  if x == "dog":
    continue
  print(x)