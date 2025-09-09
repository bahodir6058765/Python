# 1. Raqamni nolga bo'lishda ZeroDivisionError istisnosini hal qilish uchun Python dasturini yozing.
a = int(input("a ga qiynat kiriting:"))
for i in range(1,10):
    if a > 10:
        print(f"{i} ga bo'lgandagi qoldiq: {a%i}")
    elif 1 < a <= 10:
        if i <= a:
            print(f"{i} ga bo'lgandagi qoldiq: {a%i}")
        elif i > a:
            break
          # 2. Foydalanuvchini butun sonni kiritishni taklif qiladigan va agar kiritilgan butun son bo'lmasa, ValueError istisnosini ko'taradigan Python dasturini yozingn 
try:
    n = int(input("n ni kiriting:"))
    if type(n) == int:
        print("Butun son")
    else:
        print("Butun emas")
except:
    print("Siz ValueError bilan xato qildingiz!")

# 3. Faylni ochadigan va fayl mavjud bo'lmasa FileNotFoundError istisnosini boshqaradigan Python dasturini yozing.
try:
    with open("test.txt", 'r') as f:
        print("Fayl topildi")
except:
    print("Siz FileNoteFaundError xatoligiga yo'l qo'ydingiz!")

# 4. Foydalanuvchiga ikkita raqam kiritishni taklif qiladigan va agar kirishlar sonli bo'lmasa, TypeError istisnosini ko'rsatadigan Python dasturini yozing.
try:
    n = int(input("n ni kiriting:"))
    m = int(input("m ni kiriting:"))
    print("Siz son kiritdingiz")
except:
    print("Siz ValueError bilan xato qildingiz!")

# 6. Ro'yxatda amalni bajaradigan va indeks diapazondan tashqarida bo'lsa, IndexError istisnosini boshqaradigan Python dasturini yozing.
try:
    indeks = int(input("Sizga kerakli element indeksini kiriting!"))
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{indeks}-element: {ls[indeks]}")
except:
    print(f"Ro'yxatda {len(ls)} ta element bor siz kiritgan indeks bo'yicha element topilmadi")

# 7. Foydalanuvchiga raqam kiritishni taklif qiladigan va agar foydalanuvchi kiritishni bekor qilsa, 
# KeyboardInterrupt istisnosini boshqaradigan Python dasturini yozing.
try:
    x = input("n ga butun qiymat kiriting: ")

    if x == "":
        print("Siz hech narsa kiritmadingiz!")
    else:
        n = int(x)
        print("Siz kiritgan son:", n)

except ValueError:
    print("Iltimos, faqat butun son kiriting!")

except KeyboardInterrupt:
    print("\nSiz ma'lumot kiritishdan bosh tortdingiz (Ctrl+C bosildi).")


# 8. Agar arifmetik xato bo'lsa, bo'linishni bajaradigan va ArithmeticError istisnosini boshqaradigan Python dasturini yozing.
try:
    a = 100
    for i in range(11):
        s = a // i
        print(s)
except ArithmeticError:
    print("Siz 0 ga bo'lishga urindingiz bu xato !!!")
  # 9. Agar kodlash muammosi bo'lsa, faylni ochadigan va UnicodeDecodeError istisnosini boshqaradigan Python dasturini yozing.
try:
    # UTF-8 kodlash bilan ochishga urinib ko'ramiz
    with open("namuna.txt", "r") as f:
        data = f.read()
    print("Fayl muvaffaqiyatli o‘qildi!")

except UnicodeDecodeError:
    print("Xatolik: Faylni UTF-8 kodlashda o‘qib bo‘lmadi.")
    print("Boshqa encoding bilan ochishga urinib ko‘raylik...")
    # Yana bir variant sifatida latin1 kodlash bilan ochish
    with open("namuna.txt", "r", encoding="latin-1") as f:
        data = f.read()
    print("Fayl latin-1 kodlash bilan o‘qildi!")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi!")

# 12. Faylga ro'yxat yozish uchun Python dasturini yozing.
ls = ["Python", "STATA", "C++", "Java", "JavaScript"]
with open("Uzbekistan.txt", 'a', encoding="utf-8") as f:
    f.write(", ".join(ls) + "\n")  # ro‘yxatni string qilib yozadi
# 13. Fayl mazmunini boshqa faylga nusxalash uchun Python dasturini yozing.
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read()
with open("Uzbekistan.txt", 'w', encoding="utf-8") as f:
    f.write("".join(data) + "\n")
with open("Uzbekistan.txt", 'r', encoding="utf-8") as f:
    new_data = f.read()
    print(new_data)


# 14. Birinchi fayldagi har bir satrni ikkinchi fayldagi tegishli qator bilan birlashtirish uchun Python dasturini yozing.
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
with open("Uzbekistan.txt", 'a', encoding="utf-8") as f:
    f.write("".join(data) + "\n")


# 15. Birinchi fayldagi har bir satrni ikkinchi fayldagi tegishli qator bilan birlashtirish uchun Python dasturini yozing.
with open("namuna.txt", "r", encoding="utf-8") as f1, open("Uzbekistan.txt", "r", encoding="utf-8") as f2:
    satrlar1 = f1.readlines()
    satrlar2 = f2.readlines()

# Birlashtirilgan satrlarni yangi faylga yozish
with open("birlashtirilgan.txt", "w", encoding="utf-8") as chiqish:
    for s1, s2 in zip(satrlar1, satrlar2):   # har bir qatorni moslashtirib oladi
        chiqish.write(s1.strip() + " " + s2.strip() + "\n")

print("Fayllar muvaffaqiyatli birlashtirildi ✅")

# 16. Fayldan tasodifiy qatorni o'qish uchun Python dasturini yozing.
import random

# Faylni ochamiz
with open("namuna.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()  # barcha qatorlarni ro'yxatga o'qiymiz

# Tasodifiy qator tanlaymiz
tasodifiy_qator = random.choice(qatorlar)

print("Tasodifiy qator:", tasodifiy_qator.strip())  # strip() qator oxiridagi \n ni olib tashlaydi


# 18. Matn faylini kirish sifatida qabul qiladigan va berilgan matn faylidagi so'zlar sonini qaytaradigan Python dasturini yozing. 
# Eslatma: Ba'zi so'zlarni bo'sh joysiz vergul bilan ajratish mumkin.

with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read().split()
    s = 0
    for i in data:
        s += 1
    print(f"Ro'yxat {s} ta so'z bor")

# 19. Turli matnli fayllardan belgilar ajratib olish va ularni roʻyxatga qoʻyish uchun Python dasturini yozing.
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read()
    maxsus_belgi = []
    for belgi in list(data):
        if belgi == "-":
            maxsus_belgi.append(belgi)
    print(maxsus_belgi)

# 20. A.txt, B.txt va hokazo nomli 26 ta matnli fayllarni Z.txt gacha hosil qilish uchun Python dasturini yozing.

import string

harflar = list(string.ascii_uppercase)  # A–Z
for i in harflar:
    with open(f"{i}.txt", 'w', encoding='utf-8') as f:
        f.write(f'{i}')
