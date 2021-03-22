Email = input("Enter Your Email : ").strip()

username = Email[:Email.index('@')]
print(f"User Name : {username}")

domain = Email[Email.index('@')+1:]
print(f"Domain Name : {domain}")
