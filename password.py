password = input()

valid = False

if ((len(password) >= 8) and (len(password) <= 32)):
  if ((password[0].isupper()) or (password[0].islower())):
    if ((not(password.find('/') != -1)) and 
    (not(password.find('\\') != -1)) and 
    (not(password.find('=') != -1)) and 
    (not(password.find('\'') != -1)) and 
    (not(password.find('\"') != -1)) and 
    (not(password.find(' ') != -1))):
      valid = True
  else:
    valid = False
else:
  valid = False

print(valid)