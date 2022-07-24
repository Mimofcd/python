from item import Item
from shoppingbasket import ShoppingBasket

tomatoSoup = Item("Tomato Soup","200mL can", 0.70,55)
spaghetti = Item("Spaghetti","500g pack", 1.10,8)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,8)
mozarella = Item("Mozarella","100g", 1.50,9)
gratedCheese = Item("Grated Cheese","100g",2.20,11)

myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)
myBasket.removeItem(tomatoSoup,9)
myBasket.addItem(spaghetti,5)



myBasket.view()