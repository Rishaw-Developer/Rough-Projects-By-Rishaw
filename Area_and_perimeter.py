select = input("Enter the shape name : ")
choose = input("Enter the what you want : ")

class Shape():

    def message(self):
        return "This feature is not available now. We are developing it."

    if select == "rectangle":
        
        def __init__(self , l , b):
            if choose == "area":
                self.area = l * b

            elif choose == "perimeter":
                self.perimeter = 2 * (l + b)

            else:
                print("Invalid")

    elif select == "square":

        def __init__(self, side):
            if choose == "area":
                self.area = side ** 2

            elif choose == "perimeter":
                self.perimeter = 4 * side

            else:
                print("Invalid")

    elif select == "trapezium":

        def __init__(self ,h , a , b):
            if choose == "area":
                self.area = h * ( a + b ) / 2

            else:
                print("Invalid")

    elif select == "rhombus":

        def __init__(self, p , q):
            if choose == "area":
                self.area = p * q / 2

            else:
                print("Invalid")

    elif select == "quadrilateral":

        def __init__(self, d , h1 , h2):

            if choose == "area":
                self.area = d * (h1 + h2) / 2
            
            else:
                print("Invalid")

    else:
        print("This shape is not available")
if select == "rectangle":
    length = int(input("Enter the length: "))
    wide = int(input("Enter the width: "))

    React = Shape(int(length), int(wide))

    if choose == "area":
        print(React.area)

    elif choose == "perimeter":
        print(React.perimeter)

    else:
        print("invalid")

elif select == "square":
    side = int(input("Enter the side: "))

    Square = Shape(side)

    if choose == "area":
        print(Square.area)

    elif choose == "perimeter":
        print(Square.perimeter)

    else:
        print("invalid")

elif select == "trapezium":
    h = int(input("Enter the height: "))
    a = int(input("Enter the length of base of trapezium: "))
    b = int(input("Enter the length of upper part of trapezium: "))

    Trapezium = Shape(h , a, b)

    if choose == "area":
        print(Trapezium.area)

    elif choose == "perimeter":
        print(Trapezium.message())

    else:
        print("invalid")

elif select == "rhombus":
    p = int(input("Enter the length of the first diagonal: "))
    q = int(input("Enter the length of the second diagonal: "))

    rhombus= Shape(p, q)

    if choose == "area":
        print(rhombus.area)

    elif choose == "perimeter":
        print(rhombus.message())

    else:
        print("invalid")

elif select == "quadrilateral":
    d = int(input("Enter the length of the diagonal: "))
    h1 = int(input("Enter the length of the first height: "))
    h2 = int(input("Enter the length of the second height: "))

    quadrilateral = Shape(d , h1 , h2)

    if choose == "area":
        print(quadrilateral.area)

    elif choose == "perimeter":
        print(quadrilateral.message())

    else:
        print("invalid")



else:
    print("Invalid")