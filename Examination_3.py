# ==========================================
# โจทย์ข้อที่ 3: หาค่ามากที่สุดจากตัวเลข 3 จำนวน
# Input: ตัวเลขจำนวนเต็ม 3 บรรทัด
#        บรรทัดที่ 1 ตัวเลข A
#        บรรทัดที่ 2 ตัวเลข B
#        บรรทัดที่ 3 ตัวเลข C
# Output: ตัวเลขที่มีค่ามากที่สุด
# ตัวอย่าง: A = 15, B = 42, C = 8 -> ผลลัพธ์คือ 42
# ==========================================

# นักเรียนเขียนโค้ดต่อจากบรรทัดนี้


a_number = int(input("ตัวเลข A: "))
b_number = int(input("ตัวเลข B: "))
c_number = int(input("ตัวเลข C: "))

if a_number >= b_number and a_number >= c_number:
    print(a_number)

elif b_number >= a_number and b_number >= c_number:
    print(b_number)
    
else:
    print(c_number)
