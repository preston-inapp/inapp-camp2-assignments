from random import randint

products = []

class Warehouse:
    def getProductCount(self, name, category):
        count = 0
        for product in products:
            if (product["Name"] == name and product["category"] == category):
                count += 1
        return str(count)

    def __init__(self, name, cat, bprice, tax, dis, mrp):
        self.name = name.upper()
        self.category = cat.upper()
        self.productCode = "{}{}{}{}".format(self.name[0:2], self.cat[0:2], self.getProductCount(name, category), randint(100,999))
        self.bprice = bprice
        self.tax = tax
        self.dis = dis
        self.mrp = mrp


while(True):

    print("""1. List
             2. Add a product
             3. Exit"""
    )
    
    match int(input("CHOICE >> ")):
        case 1:
            print("Products")
        
        case 2:
            name = input("Enter name of the product : ")
            category = input("Enter category name : ")
            bprice = float(input("Enter basic price : "))
            tax = float(input("Enter tax : "))
            dis = float(input("Enter discount : "))
            mrp = float(input("Enter MRP : "))
            new_product = Warehouse(name, category, bprice, tax, dis, mrp)
            products.append(new_product)
        case 9:
            exit()
        case _:
            print("Invalid entry")
