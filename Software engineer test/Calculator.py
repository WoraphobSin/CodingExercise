class Calculator:
    def __init__(self, channel):
        self.channel = channel
        self.product = {}
        self.recives = {}
    
    def addProduct(self, id, set, price):
        self.product[id] = {"Set" : set, "Price" : price}
        # print("Product added successfully.")

    def showProduct(self):
        keys = list(self.product)
        for x in range(0,len(keys)):
            print(f"ID {keys[x]}\t{self.product[keys[x]]}")
        print("\nOrder doubles of Orange, Pink or Green sets will get a 5% discount for each bundles(not in total) !!!")

    def order(self):
        keys = list(self.product)   
        while(True):
            print("What set do you want to buy?\nENTER set ID ")
            a = int(input())
            for x in range(0,len(keys)):
                if a == keys[x]:
                    print("How many do you want?")
                    b = int(input())
                    self.recives[a]=b   
            print("Do you want to add another set?\nyes or no?")
            if "no" == str(input()):
                break
        # print(self.recives)
        quantitly = list(self.recives)
        calTotal = self.recives.copy()
        # print(quantitly)
        print("Do you have a member card?\nIf you have a member card you will get 10% discount on total !\nyes or no?")               
        if "yes" == str(input()):
            print("Your orders are")
            for z in range(0,len(quantitly)):
                if quantitly[z] == 202 or quantitly[z] == 505 or quantitly[z] == 707:
                    if self.recives[quantitly[z]]%2 == 0:
                        print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                        +str(0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]))
                        calTotal.update({quantitly[z]:0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]})
                        # calTotal[quantitly[z]] = 0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                    else:
                        if self.recives[quantitly[z]] > 1 :
                            print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                            +str((0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.product[quantitly[z]]["Price"]))
                        else:
                            print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                            +str(((self.recives[quantitly[z]])*self.product[quantitly[z]]["Price"])))
                        
                        calTotal.update({quantitly[z]:(0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.product[quantitly[z]]["Price"]})
                        # calTotal[quantitly[z]] = (0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                else:
                    print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                    +str(self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]))
                    calTotal.update({quantitly[z]:self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]})
                    # calTotal[quantitly[z]] = self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                    
            total = 0
            for z in range(0,len(quantitly)):
                total = total + calTotal[quantitly[z]]
            print(f"Total = {total} THB\nTotal with 10% discount = {total*0.9} THB")
            
            # print(self.recives)
            # print(calTotal)
            
        else:
            print("Your orders are")
            for z in range(0,len(quantitly)):
                if quantitly[z] == 202 or quantitly[z] == 505 or quantitly[z] == 707:
                    if self.recives[quantitly[z]]%2 == 0:
                        print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                        +str(0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]))
                        calTotal.update({quantitly[z]:0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]})
                        # calTotal[quantitly[z]] = 0.95*self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                    else:
                        if self.recives[quantitly[z]] > 1 :
                            print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                            +str((0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.product[quantitly[z]]["Price"]))
                        else:
                            print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                            +str(((self.recives[quantitly[z]])*self.product[quantitly[z]]["Price"])))
                        
                        calTotal.update({quantitly[z]:(0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.product[quantitly[z]]["Price"]})
                        # calTotal[quantitly[z]] = (0.95*(self.recives[quantitly[z]]-1)*self.product[quantitly[z]]["Price"])+self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                else:
                    print("- " + self.product[quantitly[z]]["Set"] + "\tQauntity "+ str(self.recives[quantitly[z]]) + "\tPrice "+ str(self.product[quantitly[z]]["Price"])+"\tTotal "\
                    +str(self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]))
                    calTotal.update({quantitly[z]:self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]})
                    # calTotal[quantitly[z]] = self.recives[quantitly[z]]*self.product[quantitly[z]]["Price"]
                    
            total = 0
            for z in range(0,len(quantitly)):
                total = total + calTotal[quantitly[z]]
            print(f"Total = {total} THB")
            
            # print(self.recives)
            # print(calTotal)





