import base64

def encrypt_password(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)

user_pass = input("Enter ur PW:")
encrypt_password(user_pass)