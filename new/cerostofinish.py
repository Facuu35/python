user_input = input("Type your numbers buddy: ")


numbers = [num for num in user_input]
print(numbers)
non_zero = [num for num in user_input if num != 0]
print(non_zero)
zero = [num for num in user_input if num == 0]
print(zero)
result = non_zero + zero

print(result) 