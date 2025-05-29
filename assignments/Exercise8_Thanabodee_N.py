
dbusername= "admin"
dbpassword="123"
username = input("Username: ")
password = input("Password: ")
if username == dbusername and password == dbpassword:
    print("Done")
    print("----------Shop----------")
    print("banana: 10 THB")
    print("apple: 20 THB")
    print("-------------------------")
    product = input("Product: ")
    amount = int(input("Amount: "))
    if product == "banana": 
        print("Price: ",amount *10)
    elif product == "apple":
        print("Price: ",amount *20)
    else:
        print("error")
else:
    print("ข้อมูลไม่ถูกต้อง")


# แบบที่2

# # รายการสินค้า
# product_list = ['apple', 'mango', 'orange', 'banana', 'grape']
# # ราคาสินค้า (เรียงตามลำดับเดียวกับ product_list)
# product_price = [20, 30, 15, 10, 30]

# # ข้อมูลเข้าสู่ระบบ
# dbusername = "admin"
# dbpassword = "123"

# # รับข้อมูลจากผู้ใช้
# username = input("Username: ")
# password = input("Password: ")

# # ตรวจสอบชื่อผู้ใช้และรหัสผ่าน
# if username == dbusername and password == dbpassword:
#     print("login Succes!")

#     # รับชื่อสินค้าและจำนวนที่ต้องการ
#     product = input("Enter product name: ")
#     amount = int(input("Enter amount: "))

#     # ตรวจสอบว่าสินค้ามีอยู่ในรายการหรือไม่
#     if product in product_list:
#         # หาตำแหน่งของสินค้าที่ตรงกัน
#         indexs = product_list.index(product)

#         # ดึงราคาสินค้าจากตำแหน่งเดียวกันใน product_price
#         price = product_price[indexs]

#         # คำนวณราคารวมก่อน vat
#         amount_price = price * amount

#         # กำหนด VAT 7%
#         vat = 7

#         # คำนวณราคารวมที่รวม VAT แล้ว
#         result = amount_price + (amount_price * vat / 100)

#         # แสดงผล
#         print("------PRODUCT INFORMATION------")
#         print(f"|             Product: {product}        |")
#         print(f"|              Amount:  {amount}           |")
#         print(f"|               Price: {amount_price} THB       |")
#         print(f"|  Price(include vat): {result:.2f}        |")
#         print("-------------------------------")
#     else:
#         # ถ้าไม่พบสินค้า
#         print("Product not found")
# else:
#     # ถ้าชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง
#     print("user error")
