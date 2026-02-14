import hashlib
username = input("Enter username: ")
password = input("Enter password: ")
stored_password = hashlib.sha256("2007".encode()).hexdigest()
entered_password = hashlib.sha256(password.encode()).hexdigest()
if username == "sushmidha" and entered_password == stored_password:
    print("Login successful")
else:
    print("Invalid credentials")