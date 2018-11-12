
email = input("What is your Email:")

#Username
username = email[:email.index("@"):1]
print(username)

#Domain
domain = email[email.index('@') + 1:email.index('.com')]
print(domain)

