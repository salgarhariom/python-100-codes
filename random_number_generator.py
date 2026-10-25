import random
a=int(input("enter how many random numbers do you need?: "))
print("generated random numbers: ")
for i in range(a):
    print(random.randint(1,100))