def printDenominations(amt):
    denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    print("The denominations are : ")
    for i in denominations:
        print("Rs. {} : {} nos".format(i, amt//i))
        amt = amt % i

amt = int(input("Enter amount : "))
printDenominations(amt)