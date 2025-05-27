# รับค่าระยะทางและเวลา
distance = int(input("Enter distance (km): "))
time = int(input("Enter time (hr): "))

# คำนวณอัตราเร็ว
speed = distance / time

# แสดงผลลัพธ์
print(f"{int(speed)} km/h")
