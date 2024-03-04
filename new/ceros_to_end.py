from collections import Counter

list = [1, 0, 8, 9, 8, 4, 0, 0, 6, 5, 46, 12, 5, 15, 22, 0, 123, 0, 5, 159, 123, 226, 891, 11, 101, 111, 1596]


for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print(f"Original list:\n {list}")

sorted_list = sorted(list)
print(f"Sorted List. Smallest to largest:\n{sorted_list}")

even_numbers = [num for num in list if num % 2 == 0]
odd_numbers = [num for num in list if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

occurrences = Counter(list)
print("Occurrences of each number:", occurrences)

list_sum = sum(list)
list_average = sum(list) / len(list)
list_max = max(list)
list_min = min(list)
print("Sum:", list_sum)
print("Average:", list_average)
print("Maximum:", list_max)
print("Minimum:", list_min)
