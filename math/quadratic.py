import math

a = int(input("Enter Value For 'a' : "))
b = int(input("Enter Value For 'b' : "))
c = int(input("Enter Value For 'c' : "))

# b square
bSquare = b ** b

discriminant = bSquare - (4 * a * c)

if discriminant > 0:
    x1 = (-b - math.sqrt(discriminant)) / (2 * a)
    x2 = (-b + math.sqrt(discriminant)) / (2 * a)

    print("Possible Solution Sets")
    # this shows two different pairs for set values using ceil and floor methods
    print("Solution sets are {0} and {1}".format(math.ceil(x1), math.ceil(x2)))
    print("Solution sets are {0} and {1}".format(math.floor(x1), math.floor(x2)))
else:
    print("Solution Set Not Possible")
