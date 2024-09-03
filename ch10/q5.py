class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def status(A):
        print(f"Name of the Train is : {A.name}")
        print(f"Price of the Ticket is Rs.{A.fare}")
    def fareInfo(B):
        print(f"No of seats avilable of the Train is : {B.seats}")
    def bookTicket(C):
        if C.seats>0:
            print(f"Your Ticket havebeen booked and your seat No : {C.seats}")
            C.seats-=1
        else:
            print(F"Sorry! there is no ticket avilable so Try in 'KARAMANDAL EXPRESS'")    
   
        
train1=train("UKTAL EXPRESS",500,20)
train1.status()
train1.fareInfo()
train1.bookTicket()
train1.bookTicket()
train1.bookTicket()
train1.fareInfo()


