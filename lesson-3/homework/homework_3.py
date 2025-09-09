## 1. Create and Access List Elements Create a list containing five different fruits and print the third fruit.

txt=["anor", "gilos", "shaftoli", "olma", "nok"]
print(txt[2])

## 2. Concatenate Two Lists Create two lists of numbers and concatenate them into a single list.
ls1=[1,2,3,4,5,6,7,8,9,]
ls2=[10,11,12,13,14,15,16,17,18,19,20]
ls1.extend(ls2)
print(ls1)

## 3. Extract Elements from a List Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

number=["1","2","3","4","5"]
print(number[0])
print(number[2])
print(number[4])

##4. Convert List to Tuple Create a list of your five favorite movies and convert it into a tuple.
film=["john wick", "bgbkgm", "nvfbvfv", "fvjhvbh", "vnfuivh"]
filmlar = tuple(film)
print(filmlar)

## 5. Check Element in a List Given a list of cities, check if "Paris" is in the list and print the result.
shahar= ["Tashkent", "Paris", "Dubai"]
shahar2= input("Shaharni kirit")
if shahar2 in shahar:
    print("Topdingiz")
else:
    print("Topa olmading")

## 6. Duplicate a List Without Using Loops Create a list of numbers and duplicate it without using loops.

ls = [1,2,3,4,5]
ls.append("Madrid")
ls.insert(0,"Barcelona")
print(ls)

## 7. Swap First and Last Elements of a List Given a list of numbers, swap the first and last elements.
ls=[1,2,3,4,5,6,7,8,9,10]
ls[len(ls)-1],ls[0]=ls[0],ls[len(ls)-1]
print(ls)

## 8. Slice a Tuple Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers=(1,2,3,4,5,6,7,8,9,10)
bolak=numbers[2:7]
print(bolak)


## 9. Count Occurrences in a List Create a list of colors and count how many times "blue" appears in the list.
colours = ['blue', 'red', 'blue', 'yellow', 'green', 'blue', 'green']
son = colours.count('blue')
print(son)

## 10. Find the Index of an Element in a Tuple Given a tuple of animals, find the index of "lion".
animals = ("tiger", "elephant", "lion", "giraffe", "zebra")
index_of_lion = animals.index("lion")
print(index_of_lion)

## 11. Merge Two Tuples Create two tuples of numbers and merge them into a single tuple.
num1=(1,2,3,4)
num2=(5,6,7,8)
qoshish=num1+num2
print(qoshish)

## 12. Ro‘yxat va to‘plam uzunligini toping Roʻyxat va kortej berilgan boʻlsa, ularning uzunligini toping va chop eting.
ls = [2, 3, 5, 4, 6, 10, 4, 5, 3, 11, 12, "Yo'lbars", "Sirtlon", "Qoplon"]
kartej = (2, 3, 5, 4, 6, 10, 4, "Maymun", "Sher", "Jirafa",)
ls_uzunligi = len(ls)
kartej_uzunligi = len(kartej)
print("Ro'yxat uzunligi:", ls_uzunligi, "\nKartej uzunligi:", kartej_uzunligi)

## 13. Tupleni ro'yxatga aylantirish (Beshta raqamdan iborat kortej yarating va uni ro'yxatga aylantiring.)
kartej = (4, 5, 3, 11, 12)
royxat  = list(kartej)
print(royxat)

## 14. Tupledagi maksimal va minimal qiymatlarni toping (Raqamlar majmuasi berilgan, maksimal va minimal qiymatlarni toping va chop eting.)
kartej = (2, 3, 5, 8, 10, 12, 22, 32, 44)
print("min:", min(kartej), "\nmax:", max(kartej))

## 15. Tupleni teskari o'zgartirish (So'zlar to'plamini yarating va uni teskari tartibda chop eting.)
kartej = ("Sanjar", "Akmal", "Nodir")
teskari = tuple(reversed(kartej))
print(teskari)
