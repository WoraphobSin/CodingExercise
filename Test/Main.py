from Calculator import *

#Create Calculator
oCalculator1 = Calculator(1)

#Add Product
oCalculator1.addProduct(101, "Red set", 50)
oCalculator1.addProduct(202, "Green set", 40)
oCalculator1.addProduct(303, "Blue set", 30)
oCalculator1.addProduct(404, "Yellow set", 50)
oCalculator1.addProduct(505, "Pink set", 80)
oCalculator1.addProduct(606, "Purple set", 90)
oCalculator1.addProduct(707, "Orange set", 120)

oCalculator1.showProduct()
oCalculator1.order()