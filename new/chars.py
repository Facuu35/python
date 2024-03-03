allwed_chars = set("qwertyuioplkjhgfdsazxcvbnm")
user_input = input("Type your name:")

if set(user_input).issubset(allwed_chars):
    print("Valid username")
else:
    print("no sir")