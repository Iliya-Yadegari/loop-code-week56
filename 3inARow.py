from random import randint

random_num = randint(1,6)
count = 0

f = 0

if random_num % 2==1:
    count += 1
    
print("Let's roll some dice!")
print(f"You rolled a {random_num}")

while True:
    f+= 1
    
    if count == 3:
        print(f"Three in a row in {f} rolls")
        break
    
    n = randint(1,6)
    
    print(f"You rolled a {n}")
    
    if n%2==1:
        count += 1
    else:
        cnt = 0