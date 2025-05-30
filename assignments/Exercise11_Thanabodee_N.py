# รับค่าจำนวนแถวจากผู้ใช้
num = int(input("Enter a number: "))

# ลูปควบคุมแต่ละแถว (เช่น i = 1 ถึง num)
for i in range(1, num + 1):

    # ลูปพิมพ์ช่องว่าง เพื่อให้ดาวอยู่ตรงกลาง (ซ้ายมือ)
    # เช่น ถ้า i = 1 และ num = 5 → ช่องว่าง = 4
    for space in range(num - i):
        print(" ", end="")  # ไม่ขึ้นบรรทัดใหม่

    # ลูปพิมพ์ดาวในแต่ละแถว
    # จำนวนดาวต่อแถวคือ 2*i - 1 → ได้เป็นเลขคี่ (1, 3, 5, 7, ...)
    for star in range(2 * i - 1):
        print("*", end="")  # ไม่ขึ้นบรรทัดใหม่

    # พอพิมพ์ครบทั้งช่องว่างและดาว → ขึ้นบรรทัดใหม่
    print()
