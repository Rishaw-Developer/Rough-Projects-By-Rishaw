length = int(input("Enter the length: "))
wide = int(input("Enter the width: "))

choose = input("Enter the shape name: ")

def rect(l, w):

    choose = input("Enter what you want : ")

    def area(a ,b):
        return a * b
        

    def perimeter(a,b):
        return 2 * (a + b)
    
    if choose == "area":
        print(area(l , w))

    elif choose == "perimeter":
        print(perimeter(l, w))


if choose == "rectangle":
    rect(length , wide)
