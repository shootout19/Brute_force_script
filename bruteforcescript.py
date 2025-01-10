import itertools

target_password = input("Enter Password : ") # Enter Password You Find 
length = len(target_password)

tar = ""
for i in range(97, 123):  # Add a to z
    tar += chr(i)
for i in range(65, 91):  # Add A to Z
    tar += chr(i)
for i in range(10):  # Add 0 to 9
    tar += str(i)


passwords = itertools.product(tar, repeat=length)

for i in passwords:
    i = ''.join(i)
    print(f"[*] Checking For Password : {i}")
    if i == target_password:
        print(f"[*] Password Password Found : {i}")
        break