from re import I
from tkinter import N
from item import Item
class ShoppingBasket:
    def __init__(self):
        self.items={}
        self.checkout=False
    def addItem(self,item,quantity=1):
        if (item.stock-quantity)>=0:
            if quantity>0:
                if item in self.items:
                    self.items[item]+=quantity
                else:
                    self.items[item]=quantity
            else:
                print("Invalid operation. Quantity must pe positive!")
        else: 
            print("No stock for "+str(item.name))
    def removeItem(self,item,quantity=0):
        if quantity<=0:
            self.items.pop(item,None)
        else:
            if item in self.items:
                if quantity<self.items[item]:
                    self.items[item]-=quantity
                else:
                    self.items.pop(item,None)
                    
    def updateItem(self,item,quantity):
        if quantity>0:
            self.items[item]=quantity
        else:
            self.removeItem(item)
    def view(self):
        totalCost=0
        print("----------")
        for item in self.items:
            quantity=self.items[item]
            item.stock=item.stock-quantity
            cost=quantity*item.price
            print(" + "+item.name+" - "+str(quantity)+" x EUR" + str(item.price) + " = " + str(cost))
            print(" + "+item.name+" remain in stock:  "+str(item.stock)+" items")
            totalCost+=cost
        print("---------")
        print("Total cost: "+str(totalCost))