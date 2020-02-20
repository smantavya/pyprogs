#input email address
email = str(input("enter your email address = "))

username = email[:email.index('@')]
print("Your Username is " + username)

domain = email[email.index('@')+1:email.index('.')]
print("Your Domain is " + domain)
