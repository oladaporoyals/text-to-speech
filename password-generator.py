import random

#define the characters to be used for the password 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

while 1:
    #set password length
    password_len = int(input("how long do you want your password to be :"))
   #set password count
    password_count = int(input("how many passwords do you want :"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("here is password:" + password)
