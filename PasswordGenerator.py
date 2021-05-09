'''
Tyler Schuler
Python Random Password Generator. 
Generates a random passowrd based on user input, hashes the password, then writes the password and hash to a CSV.
May 2021
'''
import sys
import os
import random
import csv # CSV Library
import hashlib
import pandas as pd



chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
p = []
h = []

password_len = int(input("What length password do you want : "))
password_count = int(input("How many passwords do you need : "))
for x in range(0,password_count):
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password      = password + password_char #Generates a randomized password
    p.append(password)
    
for password in p:
    result = hashlib.sha256(password.encode()) #Hashes the random password
    Hash = result.hexdigest()
    h.append(Hash)

print(h)
print(p)

df = pd.DataFrame(p, columns=['Password'])
df['Hash'] = h
print(df)
df.to_csv(r'C:\Users\Administrator\Desktop\PassManager.csv', index = False) #Input will need to reflect where the user wants the CSV saved to. 
            

        


    
    

