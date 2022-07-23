student_record = dict()

def create(roll, name, m_eng, m_phy, m_chem, m_mat, m_prog):
    if roll not in student_record.keys():
        student_record.update({roll:[name, m_eng, m_phy, m_chem, m_mat, m_prog]})
        print("1 student added")
    else:
        print("user exists")

def delete(roll):
    if roll in student_record.keys():
        del student_record[roll]
        print("1 student deleted")
    else:
        print("student does not exist")

def modify(roll, name, m_eng, m_phy, m_chem, m_mat, m_prog):
    if roll in student_record.keys():
        student_record.update({roll:[name, m_eng, m_phy, m_chem, m_mat, m_prog]})
        print("1 student modified")
    else:
        print("user does not exist")

def displayAll():
    print("Roll\t\tName")
    for i in student_record.keys():
        print("{}\t\t{}".format(i, student_record[i][0]))

def displayOne(roll):
    print("Name :", student_record[roll][0])
    print("English :", student_record[roll][1])
    print("Physics :", student_record[roll][2])
    print("Chemistry :", student_record[roll][3])
    print("Maths :", student_record[roll][4])
    print("Programming :", student_record[roll][5])

while(True):
    print("1. Create student")
    print("2. Modify student")
    print("3. Delete student")
    print("4. Display student details")
    print("5. Display all students")
    print("9. Exit")
    _userselection = int(input("Your selection : "))
    match _userselection:
        case 1:
            roll = input("Enter roll no : ")
            name = input("Enter name : ")
            eng = input("Marks in English : ")
            phy = input("Marks in Physics : ")
            che = input("Marks in Chemistry : ")
            mat = input("Marks in Maths : ")
            pro = input("Marks in Programming : ")
            create(roll, name, eng, phy, che, mat, pro)
        case 2:
            roll = input("Enter roll no : ")
            name = input("Enter name : ")
            eng = input("Marks in English : ")
            phy = input("Marks in Physics : ")
            che = input("Marks in Chemistry : ")
            mat = input("Marks in Maths : ")
            pro = input("Marks in Programming : ")
            modify(roll, name, eng, phy, che, mat, pro)
        case 3:
            roll = input("Enter roll no : ")
            delete(roll)
        case 4:
            roll = input("Enter roll no : ")
            displayOne(roll)
        case 5:
            displayAll()
        case 9:
            break
        case _:
            print("Invalid entry")