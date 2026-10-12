print("Welcome to the birthday finder")

set1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
set2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
set4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
set5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
lst = list(map(int, input("orderly type 1 for yes and 0 for no for each set you see your birthdate").split()))
numbers=[1, 2, 4, 8, 16]
total=0

for i in range(5):
    if lst[i] == 0:
        continue
    total=total+numbers[i]

print(f"Your birthday is the day of {total}")