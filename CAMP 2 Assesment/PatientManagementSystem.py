import pyodbc

def validateAndReturn(string):
    if len(string) != 0:
        return string
    else:
        return validateAndReturn(input("Previous entry invalid\nPlease enter again : "))

def validateAndReturnInt(num):
    if len(num) != 0:
        return int(num)
    else:
        return int(validateAndReturn(input("Previous entry invalid\nPlease enter again : ")))


class Hospital:
    def __init__(self):
        self.connString = 'Driver={SQL Server};Server=DESKTOP-DH4N9T0\SQLEXPRESS01;Database=inapp2;Trusted_Connection=yes;'
        self.conn = pyodbc.connect(self.connString)

    def addPatient(self, id, name, gender, age, bloodgroup):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC addPatient {}, '{}', '{}', {}, '{}'".format(id, name, gender, age, bloodgroup))
            self.conn.commit()
            return True
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            if sqlstate == '2627':
                print("ERROR: Duplicate patient id")

    def updatePatient(self, id, name, gender, age, bloodgroup):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC updatePatient {}, '{}', '{}', {}, '{}'".format(id, name, gender, age, bloodgroup))
            self.conn.commit()
            print("Updated 1 patient")
        except:
            print("update error")

    def deletePatient(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC deletePatient {}".format(id))
            self.conn.commit()
            print("Deleted 1 patient")
        except:
            print("delete error")

    def listPatients(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC listPatients")
            print("Patients\nID\t\tNAME\t\tGENDER\t\tAGE\t\tBLOODGROUP")
            for i in cursor:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0], i[1], i[2], i[3], i[4]))
        except:
            print("listing error")

    def searchPatient(self, id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("EXEC searchPatient {}".format(id))
            if(cursor.rowcount == 0):
                print("Patient not registered")
            else:
                print("ID\t\tNAME\t\tGENDER\t\tAGE\t\tBLOODGROUP")
                for i in cursor:
                    print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i[0], i[1], i[2], i[3], i[4]))
        except:
            print("search error")


kims = Hospital()

while(True):
    print("""
        1. Add Patient
        2. Update Patient
        3. Delete Patient
        4. List Patients
        5. Search Patient
        9. Exit
        """)
    match int(input("CHOICE >> ")):
        case 1:
            if kims.addPatient(
                validateAndReturnInt(input("Patient ID : ")),
                validateAndReturn(input("Name : ")),
                validateAndReturn(input("Gender : ")),
                validateAndReturn(input("Age : ")),
                validateAndReturn(input("Blood Group : "))
            ):
                print("Patient registered successfully")
            else:
                print("Failed to register patient")
        case 2:
            kims.updatePatient(
                validateAndReturnInt(input("Patient ID : ")),
                validateAndReturn(input("Name : ")),
                validateAndReturn(input("Gender : ")),
                validateAndReturn(input("Age : ")),
                validateAndReturn(input("Blood Group : "))
            )
        case 3:
            kims.deletePatient(validateAndReturnInt(input("Patient ID : ")))
        case 4:
            kims.listPatients()
        case 5:
            kims.searchPatient(validateAndReturnInt(input("Patient ID : ")))
        case 9:
            kims.conn.close()
            exit()
        case _:
            print("Invalid entry")

