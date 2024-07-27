from datetime import datetime
name = input("Enter your name: ")

# lists of items
lists = ''' 
Soap        Rs.30/piece
Colgate     Rs.50/each
Rice        Rs.1500/bag
Oil         Rs.200/litre
Salt        Rs.30/kg
Chilli      Rs.150/kg
Gingerpaste Rs.200/kg
Biscuits    Rs.20/packet
'''
# Declarations
price = 0
pricelist = []
totalprice = 0
finalprice = 0
itemlist = []
quantitylist = []
pricelists = []


#rates for items
items = {'Soap':30, 'Colgate':50, 'Rice':1500, 'Oil':200, 'Salt':30, 'Chilli':150, 'Gingerpaste':200, 'Biscuits':20}

option = int(input("For list of items press 1: "))
if option == 1:
    print(lists)
    
for i in range(len(items)):
    inp1 = int(input('If you want to buy press 1 or to exit press 2: '))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter your quantity: "))
        if item in items.keys():
            price = quantity * (items[item])
            pricelist.append((item, quantity, items, price))
            totalprice += price
            itemlist.append(item)
            quantitylist.append(quantity)
            pricelists.append(price)
            gst = (totalprice * 5)/100
            finalamount = gst + totalprice 
            
        else:
            print("Entered item is not listed above")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no: ")
    if inp == "yes":
        pass
        if  finalamount != 0:
            print(25*"=", "Pavan Supermarket", 25*"=")
            print(25*" ", "Hyderabad")
            print("Name:", name, 30*"Date", datetime.now())
            print(75*"-")
            print("sno", 8*" ", 'items', 8*" ", 'Quantity', 3*" ", 'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ', itemlist[i],3*' ', quantitylist[i],8*"", pricelists[i])
            print(75*"-")
            print(50*" ",'TotalAmount:', 'Rs', totalprice)
            print("gst amount",40*" ", 'Rs', gst)
            print(75*"-")
            print(50*" ",'finalAmount:', 'Rs', finalamount)
            print(75*"-")
            print(20*" ","Thanks for visiting us")
            print(75*"-")

            
            
                
        
        

 