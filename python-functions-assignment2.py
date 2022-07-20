addressbook = dict()

def getNameFromPhno(phno):
    for k,v in addressbook.items():
        if phno == v:
            return k

def searchno(phno):
    if phno in addressbook.values():
        print("user found - ", getNameFromPhno(phno), "-", phno)
    else:
        print("user not found")

def searchname(name):
    if name in addressbook.keys():
        print("user found - ", name, "-", addressbook[name])
    else:
        print("user not found")

def add(name, phno):
    if name not in addressbook.keys():
        addressbook.update({name:phno})
        print("1 user added")
    else:
        print("user exists")

def delete(name):
    if name in addressbook.keys():
        del addressbook[name]
        print("1 user deleted")
    else:
        print("user does not exist")

def sort():
    print("Address Book (Sorted)")
    print("Name\t\tPhone")
    for i in sorted(addressbook.keys()):
        print("{}\t\t{}".format(i, addressbook[i]))


while(True):
    print("1. Add user")
    print("2. Delete user")
    print("3. Search by name")
    print("4. Search by number")
    print("5. Sort and display")
    print("9. Exit")
    _userselection = int(input("Your selection : "))
    match _userselection:
        case 1:
            name = input("Enter name : ")
            phno = input("Enter phone no : ")
            add(name, phno)
        case 2:
            name = input("Enter name : ")
            delete(name)
        case 3:
            name = input("Enter name : ")
            searchname(name)
        case 4:
            phno = input("Enter phone no : ")
            searchno(phno)
        case 5:
            sort()
        case 9:
            break
        case _:
            print("Invalid Entry")