arr= input("Введите числа:").split()
all_unique = len(arr) == len(set(arr))
print(all_unique)