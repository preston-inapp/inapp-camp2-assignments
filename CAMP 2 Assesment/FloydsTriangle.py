def floydsTriangle(rows):
    n = 1
    for i in range(1, rows+1):
        for j in range(i):
            print(n, end="\t")
            n += 1
        print("\n")

num = int(input("Enter rows : "))
floydsTriangle(num)