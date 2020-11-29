import random , time

min = 1
max = 6

start = input("Do you want to start simulation : ")
while start == "y":

    if start == "y":
        print("We are generating a random number....")
        
        time.sleep(1.5)

        print(random.randint(min, max))

    start = input("Do you want to start simulation : ")