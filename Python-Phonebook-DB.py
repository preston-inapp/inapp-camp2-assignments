import pyodbc

class PhoneBook:

    def __init__(self, dbname, tname):
        self.dbname = dbname
        self.tname = tname
        self.connString = 'Driver={SQL Server};Server=DESKTOP-DH4N9T0\SQLEXPRESS01;Database='+dbname+';Trusted_Connection=yes;'
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tname}")
        self.pb = dict()
        for contact in cursor:
            self.pb.update({contact[0]:contact[1]})
        conn.close()

    def listContacts(self):
        print("Name\t\tPhone")
        for i in sorted(self.pb.keys()):
            print("{}\t\t{}".format(i, self.pb[i]))

    def addContact(self, name, phno):
        if name not in self.pb.keys():
            self.pb.update({name:phno})
            print("1 entry added")
        else:
            print("entry exists")

    def searchByName(self, name):
        if name in self.pb.keys():
            print("entry found - ", name, "-", self.pb[name])
        else:
            print("entry not found")
    
    def searchByNumber(self, phno):
        if phno in self.pb.values():
            for k,v in self.pb.items():
                if phno == v:
                    name = k
                    break   
            print("entry found - ", name, "-", phno)
        else:
            print("entry not found")

    def deleteContact(self, name):
        if name in self.pb.keys():
            del self.pb[name]
            print("1 entry ({}) deleted".format(name))
        else:
            print("entry does not exist")

    def commit(self):
        conn = pyodbc.connect(self.connString)
        cursor = conn.cursor()
        cursor.execute(f"TRUNCATE TABLE {self.tname}")
        for k,v in self.pb.items():
            cursor.execute("INSERT INTO {} (name, phno) VALUES ('{}', '{}')".format(self.tname, k,v))
        print("Committed edits")
        conn.commit()
        conn.close()



# book1 = PhoneBook("inapp", "phonebook")
# book1.listContacts()
# book1.addContact("Kripa", "784512")
# book1.searchByName("Kripa")
# book1.searchByNumber("465132")
# book1.deleteContact("Karikku")
# book1.commit()
# del book1
# book1 = PhoneBook("inapp", "phonebook")
# book1.listContacts()