from abc import ABC,abstractmethod
class AbstractBus(ABC):
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach=coach
        self.driver=driver
        self.arrival=arrival
        self.departure=departure
        self.from_des=from_des
        self.to=to
        self.seats=["Empty"for _ in range (20)]
class Bus(AbstractBus):
    pass

class BusCompany:
    def __init__(self) -> None:
        self.buses={}

    def install_bus(self,bus):
        print(f"Bus {bus.coach} Added Successfully")
        self.buses[bus.coach]=bus

    def display_available_buses(self):
        if not self.buses:
            print("No Buses Are Available !!")
        else:
            print(f"Coach\tDriver\tArrival\tDeparture\tFrom\tTo")
            for coach,bus in self.buses.items():
                print(f"{coach}\t{bus.driver}\t{bus.arrival}\t{bus.departure}\t{bus.from_des}\t{bus.to}")
    def book_ticket(self,coach,seat):
        if coach in self.buses:
            if 1<=seat<=20:

                if self.buses[coach].seats[seat-1]=='Empty':
                    print("Seat Booked Successfully !!")
                    self.buses[coach].seats[seat-1]=='Booked'
                else:
                    print("Seat Already Booked !!")
            else:
                print("Invalid seat Number")
        else:
            print("Invalid Coach Number")
    

    def display_sea_status(self,coach):
        if coach in self.buses:
            print(self.buses[coach].seats)

bus1=Bus(2,"Rahm","9PM","9:30","Dhaka","Sylhet")
company=BusCompany()

company.install_bus(bus1)
print(company.display_available_buses())
print(company.display_sea_status(2))



while True:
    print("Welcome to Bus Ticket Booking System!!")
    print("1. Install Bus")
    print("2. View Available Buses")
    print("3. Book Ticket")
    print("4. Check Seat Status")
    print("5. Exit")

    choice=int(input("Enter Your Choice : "))


    if choice==1:
        coach=input("Enter Bus Number : ")
        driver=input("Enter Bus Driver  Name : ")
        arrival=input("Enter Bus Arrival Time : ")
        departure=input("Enter Bus Departure Time : ")
        from_des=input("Enter Bus From Destination : ")
        to=input("Enter Bus To Destination : ")

        bus= Bus(coach,driver,arrival,departure,from_des,to)
        company.install_bus(bus)

    elif choice==2:
        company.display_available_buses()
    elif choice==3:
        coach=input("Enter Bus Number : ")
        seat=int(input("Enter Bus Number : "))


        company.book_ticket  (coach,seat)  
    elif choice==4:
        coach=input("Enter Bus Number : ")
        company.display_sea_status(coach)

    elif choice==5:
        print("Thanks For Using Our Service!!")
        break
    else:
        print("Invalid Choice")