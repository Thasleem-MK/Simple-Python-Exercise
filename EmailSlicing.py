email = input("Enter your email address: ")
index = email.index("@")
user_name = email[:index]
domain = email[index + 1 :]
print(f"Your user name is : {user_name}")
print(f"And your domain is : {domain}")
