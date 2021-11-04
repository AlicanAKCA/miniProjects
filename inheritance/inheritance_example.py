class orders():
    def __init__(self, category, orderCode,price, numberOfSales):
        self.category = category
        self.orderCode = orderCode
        self.price = price
        self.numberOfSales = numberOfSales

class tables(orders):
    pass
class chairs(orders):
    pass
class blankets(orders):
    pass
class beds(orders):
    pass


t1 = tables("kitchen","0A001","20","153")
t2 = tables("kitchen", "0A002" , "40","74")
t3 = tables("kitchen", "0A003","100","61")

c1 = chairs("kitchen", "0B001","30","141")
c2 = chairs("kitchen", "0B002","50","94")
c3 = chairs("kitchen", "0B003","70","76")

b1 = blankets("bedroom", "0C001" , "10" , "156")
b2 = blankets("bedroom", "0C002" , "30","148")
b3 = blankets("bedroom", "0C003" , "50","205")

bb1 = beds("bedroom", "0D001" , "150","29")
bb2 = beds("bedroom", "0D002" , "375","35")
bb3 = beds("bedroom", "0D003" , "550","48")

listOrders = [t1.category, t1.orderCode, t1.price, t1.numberOfSales,
t2.category, t2.orderCode, t2.price, t2.numberOfSales,
t3.category, t3.orderCode, t3.price, t3.numberOfSales,
c1.category, c1.orderCode, c1.price, c1.numberOfSales,
c2.category, c2.orderCode, c2.price, c2.numberOfSales,
c3.category, c3.orderCode, c3.price, c3.numberOfSales,
b1.category, b1.orderCode, b1.price, b1.numberOfSales,
b2.category, b2.orderCode, b2.price, b2.numberOfSales,
b3.category, b3.orderCode, b3.price, b3.numberOfSales,
bb1.category, bb1.orderCode, bb1.price, bb1.numberOfSales,
bb2.category, bb2.orderCode, bb2.price, bb2.numberOfSales,
bb3.category, bb3.orderCode, bb3.price, bb3.numberOfSales]

i = 1
a = 0
b = 1
c = 2
d = 3

while i<=12:  
    print(listOrders[a] + " kategorisindeki " + listOrders[b] + 
    " barkodlu üründen " + listOrders[c] + " dolar fiyata " +  listOrders[d] + " tane alınmıştır." )
    a += 4
    b += 4
    c += 4  
    d += 4
    i += 1

