fruit = ["apple", "mango", "peaches", "strawberry", "watermelon"]
user_input = input("enter your fruit:  ")
if user_input in fruit:
    print("we have it")
else:
    fruit.append(user_input)
    print("we do not have it", fruit)