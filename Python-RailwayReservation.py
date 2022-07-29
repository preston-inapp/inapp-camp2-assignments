import pyodbc

connString = 'Driver={SQL Server};Server=DESKTOP-DH4N9T0\SQLEXPRESS01;Database=railway;Trusted_Connection=yes;'
conn = pyodbc.connect(connString)
cursor = conn.cursor()


def listDestinations():
    cursor.execute("SELECT * FROM DESTINATIONS")
    print("Destinations\nID\tStation")
    j=1
    for i in cursor:
        print("{}\t{}".format(i[1],i[0]))

def book():
    listDestinations()
    station_number = int(input("Enter preffered Station ID : "))
    cursor.execute("EXEC getTrainsToDest {}".format(station_number))
    print("Available Trains\nTNO\t\tTrain\t\tAVLBL")
    for i in cursor:
        print("{}\t\t{}\t\t{}".format(i[0], i[1], i[2]))
    name = input("Enter your name : ")
    booked = False
    cursor.execute("EXEC getTrainsToDest {}".format(station_number))
    for i in cursor:
        if(i[2]>0):
            cursor.execute("EXEC makeBookingOnCNFM {}, {}, {}".format(name, i[0], station_number))
            print("Your booking is successful")
            conn.commit()
            booked = True
            break
    if not booked:
        cursor.execute("EXEC getTrainsToDest {}".format(station_number))
        for i in cursor:
            if(i[3]>0):
                cursor.execute("EXEC makeBookingOnWL {}, {}, {}".format(name, i[0], station_number))
                print("Your booking is successful and is currently on waiting list")
                conn.commit()
                booked = True
                break
    if not booked:
        print("Seats and waiting lists are full")
    
def listBookings():
    cursor.execute("SELECT * FROM BookingDetails")
    print("Bookings\nB_ID\tNAME\tDEST\tTRAIN\tSTATUS")
    for i in cursor:
        print("{}\t{}\t{}\t{}\t{}".format(i[0], i[1], i[2], i[3], i[4]))

while(True):
    userinput = int(input("1. Book Train\n2. List Bookings\nChoice : "))
    match userinput:
        case 1: book()
        case 2: listBookings()
        case 9: exit()
        case _: print("Invalid entry")
