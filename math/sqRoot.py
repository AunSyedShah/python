import math

upper = int(input("Enter Upper Limit: "))

print("Number\tSquare Root")

for i in range(2, upper):
    sq = math.sqrt(i)
    if sq % 2 == 0 or sq % 2 == 1:
        print("{0}\t\t{1}".format(i, sq))
