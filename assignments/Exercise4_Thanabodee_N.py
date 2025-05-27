# สร้างตัวแปรเก็บคะแนนแต่ละวิชา (สามารถเป็นทศนิยมได้)
foundation_english = float(input("Enter your score for Foundation English: "))
general_business = float(input("Enter your score for General Business: "))
intro_computer_systems = float(input("Enter your score for Introduction Computer Systems: "))
computer_programming = float(input("Enter your score for Computer Programming: "))

# แสดงผลคะแนน
print("\n--- Your Score ---")
print(f"Foundation English : {foundation_english:.2f}")
print(f"General Business : {general_business:.2f}")
print(f"Introduction Computer Systems : {intro_computer_systems:.2f}")
print(f"Computer Programming :, {computer_programming:.2f}")


# Note
## f"..." คือ f-string ใส่ค่าตัวแปรลงในข้อความได้ง่าย โดยใช้ตัวอักษร f นำหน้า และใส่ตัวแปรไว้ใน {} ใช้แทน + ได้
## :.2f คือ กำหนดให้มีทศนิยม 2ตำแหน่ง [.2 = แสดง ทศนิยม 2 ตำแหน่ง f = เป็น ตัวเลขทศนิยม (float)]
## input() คือการรับข้อมูลจากการพิมเข้าไป
