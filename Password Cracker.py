import time 

password = "888" 

print("Cracking password...")

for i in range(1000):
    guess = str(i).zfill(3)
    print("Trying password:", guess)
    time.sleep(0.05)

    if guess == password:
        print("Password found:", guess)
        break
