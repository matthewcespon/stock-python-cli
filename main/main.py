globalList = []

def importList():
    screw_list = [] #defines empty table
    myfile = open('SCREW_DATA.txt')
    for row in myfile:
        if not row.startswith("#"): #remove hashtag part
            row = row.strip('\n').split(',') #remove slash n
            screw_list.append(row)
    return screw_list

globalList = importList()

def printN(item): #return names
  return item[0], item[1], item[2]
    
      # name = printN(item)
      # name = (f"{name[0]} {name[1]} {name[2]}")

def uoStock(item): #calculate units of stock
  units100 = int(item[4])*2
  units200 = int(item[5])*4
  unitsOfStock = int(item[3]) + units100 + units200
  return unitsOfStock
      # units = uoStock(item)

def stockVal(item): #calculates stock val
    units100 = int(item[4]) * 0.9 * 2
    units200 = int(item[5]) * 0.85 * 4
    valueStock = (int(item[3]) + units100 + units200)*float(item[6])
    return valueStock
        # stockV = stockVal(item)

def bF1(sL):
    print("Screw types available: \n")
    for item in sL:
        stockV = stockVal(item)
        units = uoStock(item)
        name = printN(item)
        name = (f"{name[0]} {name[1]} {name[2]}")
        print(f"""{name}
{units} units of stock and total stock value of £{stockV:,.2f}""")

def bF2(l):
    total20 = 0
    total40 = 0
    total60 = 0
    for item in l: 
        if item[2] =="20": 
            units = uoStock(item)
            total20 += units
        if item[2] == "40":
            units = uoStock(item)
            total40 += units
        if item[2] == "60":
            units = uoStock(item)
            total60 += units
    print("20mmm screws have", total20, "units of stock")
    print("40mm screws have", total40, "units of stock")
    print("60mm screws have", total60, "units of stock")
    
def bF3(l):
    print("Please enter a length category to search (20mm, 40mm, 60mm): ")
    screwLength = input()
    print("Screws available for", screwLength + "mm\n")
    for item in l:
        if item[2] == screwLength:
            print(item[0],item[1])
            units = uoStock(item)
            stockV = stockVal(item)
            print\
(f"This screw has {units} units of stock and stock value of £{stockV:,.2f}")    


def bF4(l):
    uOption = input("""1)Increase stock levels
2)Decrease stock level (1,2)
""")
    if uOption == "1":
        screwMat = input("Please enter screw material(brass,steel): ")   
        screwHead = input("Please enter head type(slot,star,pozidriv): ")   
        screwLength = input("Please enter screw length(20,40,60mm): ")    
        screwType = [screwMat, screwHead, screwLength]
        for item in l:              
            name = printN(item)
            name = (f"{name[0]} {name[1]} {name[2]}")
            if screwType[0] == item[0]:
                if screwType[1] == item[1]:
                    if screwType[2] == item[2]:
                        uOption2 = input\
("Match Found! Would you like to update the stock of 50, 100 or 200? ")
                            
                        if uOption2 == "50":
                            incAmt = int(input\
(f"How much stock would you like to addd to {name} ? "))
                            newAmt = (int(item[3]) + incAmt)
                            item[3] = newAmt
                            indexItem = l.index(item)
                            globalList[indexItem][3] = newAmt
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][3]}")
                        if uOption2 == "100":
                            incAmt = int(input\
(f"How much stock would you like to add to {name} ? "))
                            newAmt = (int(item[4]) + incAmt)
                            item[4] = newAmt
                            indexItem = l.index(item)
                            globalList[indexItem][4] = newAmt
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][4]}")
                        if uOption2 == "200":
                            incAmt = int(input\
(f"How much stock would you like to add to {name} ? "))
                            newAmt = (int(item[5]) + incAmt)
                            item[5] = newAmt
                            indexItem = l.index(item)
                            globalList[indexItem][5] = newAmt
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][5]}")
                
                
                
    elif uOption == "2":
        screwMat = input("Please enter screw material(brass,steel): ")   
        screwHead = input("Please enter head type(slot,star,pozidriv): ")   
        screwLength = input("Please enter screw length(20,40,60mm): ")
        screwType = [screwMat, screwHead, screwLength]
        for item in l:
            name = printN(item)
            name = (f"{name[0]} {name[1]} {name[2]}")
            if screwType[0] == item[0]\
                and screwType[1] == item[1]\
                    and screwType[2] == item[2]:
                uOption2 = input\
("Match Found! Would you like to decrease the stock of 50, 100 or 200? ") 
                if uOption2 == "50":
                    decAmt = int(input\
(f"How much stock would you like to remove from {name} ? "))
                    checkIF = (int(item[3]) - decAmt)
                    costOrder = int(item[3])
                    if int(checkIF) <= 0: 
                        # if amt to decrease is more how much stock
                        uOption3 = input\
(f"This order can only be partially fulfilled, \
do you want to continue with removing {item[3]} ")
                        if uOption3 == "yes":
                            indexItem = l.index(item)
                            globalList[indexItem][3] = 0
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][3]}")
                            finalCostOrder = costOrder * float(item[6])
                            if item[7] == ' yes':
                                print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                                finalCostOrder = finalCostOrder * 0.9
                                print("Additional 10% discount applied")
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}") 
                            else:
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}") 
                        else:
                            ("Process terminated")
                            main()
                    else: # if asking amt is !> than available stock
                        newAmt = (int(item[3]) - decAmt)
                        finalCostOrder = decAmt * float(item[6]) 
                        indexItem = l.index(item)
                        globalList[indexItem][3] = 0
                        print\
(f"Success! new stock of {name} is {globalList[indexItem][3]}")
                        if item[7] == ' yes':
                            print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                            finalCostOrder = finalCostOrder * 0.9
                            print\
("Additional 10% discount applied")
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")
                        else:
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")
                            
                            
                if uOption2 == "100":
                    decAmt = int(input\
(f"How much stock would you like to remove from {name} ? "))
                    checkIF = (int(item[4]) - decAmt)
                    costOrder = int(item[4])
                    if int(checkIF) <= 0:
                        # if amt to decrease is more how much stock
                        uOption3 = input\
(f"This order can only be partially fulfilled, \
do you want to continue with removing {item[4]} ")
                        if uOption3 == "yes":
                            indexItem = l.index(item)
                            globalList[indexItem][4] = 0
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][4]}")
                            finalCostOrder = costOrder * float(item[6]) * 0.9 
                            # 10% discount for bulk purchase of 100
                            if item[7] == ' yes':
                                print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                                finalCostOrder = finalCostOrder * 0.9
                                print("Additional 10% discount applied")
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}") 
                            else:
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}") 
                        else:
                            ("Process terminated")
                            main()
                    else: # if asking amt is not more than available stock
                        newAmt = (int(item[4]) - decAmt)
                        finalCostOrder = decAmt * float(item[6]) * 0.9 
                        # 10% discount for bulk purchase of 100
                        indexItem = l.index(item)
                        globalList[indexItem][4] = 0
                        print\
(f"Success! new stock of {name} is {globalList[indexItem][4]}")
                        if item[7] == ' yes':
                            print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                            finalCostOrder = finalCostOrder * 0.9
                            print("Additional 10% discount applied")
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")
                        else:
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")

                
                                                    
                if uOption2 == "200":
                    decAmt = int(input\
(f"How much stock would you like to remove from {name} ? "))
                    checkIF = (int(item[5]) - decAmt)
                    costOrder = int(item[5])
                    if int(checkIF) <= 0:
                        # if amt to decrease is more how much stock
                        uOption3 = input\
(f"This order can only be partially fulfilled, \
do you want to continue with removing {item[5]} ")
                        if uOption3 == "yes":
                            indexItem = l.index(item)
                            globalList[indexItem][5] = 0
                            print\
(f"Success! new stock of {name} is {globalList[indexItem][4]}")
                            finalCostOrder = costOrder * float(item[6]) * 0.85 
                            # 15% discount for bulk purchase of 200
                            if item[7] == ' yes':
                                print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                                finalCostOrder = finalCostOrder * 0.9
                                print("Additional 10% discount applied")
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}") 
                            else:
                                print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")
                        else:
                            ("Process terminated")
                            main()
                    else: 
                        newAmt = (int(item[5]) - decAmt)
                        finalCostOrder = decAmt * float(item[6]) * 0.85 
                        # 15% discount for bulk purchase of 200
                        indexItem = l.index(item)
                        globalList[indexItem][5] = 0
                        print\
(f"Success! new stock of {name} is {globalList[indexItem][5]}")
                        if item[7] == ' yes':
                            print\
(f"The cost before discount £{finalCostOrder:,.2f}") 
                            finalCostOrder = finalCostOrder * 0.9
                            print\
("Additional 10% discount applied")
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")
                        else:
                            print\
(f"The cost of the final order is £{finalCostOrder:,.2f}")

                
                        
                        
def bF5(sList):
    newList = []
    for item in sList: 
        units = uoStock(item)
        newList.append(units) # appends a new list with units of stock
    maxIndex = newList.index(max(newList)) # index of highest stock
    print(f"{sList[maxIndex][0]} {sList[maxIndex][1]} {sList[maxIndex][2]}\
mm has the most stock") # prints the name of highest screw
    uOption = input("Do you want to add a 10% discount on this screw? ")
    if uOption.lower() == "yes":    
        for item in sList:
            if item[7] == ' yes':
                uOption2 = input("""
There is currently a sale running do you want to continue? """)
                if uOption2.lower() == "yes":
                    previousSale = (sList.index(item))
                    globalList[previousSale][7] = ' no'
                    globalList[maxIndex][7] = ' yes'
                else:
                    main()
    else:
        main()
 
def barChart(l):
    
    total20 = 0
    total40 = 0
    total60 = 0
    for item in l: 
        if item[2] =="20":
            units = uoStock(item)
            total20 += units
        if item[2] == "40":
            units = uoStock(item)
            total40 += units
        if item[2] == "60":
            units = uoStock(item)
            total60 += units

    screwLengths = [total20,total40,total60]
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    screwsL=['20mm','40mm','60mm']
    pos = np.arange(len(screwsL))
    
    plt.bar(pos,screwLengths,color='blue',edgecolor='black')
    plt.xticks(pos, screwsL)
    plt.xlabel('Length', fontsize=14)
    plt.ylabel('Units of Stock', fontsize=14)
    plt.title('Units of Stock in by Length',fontsize=20)
    plt.show()
 
 
def main():
    print("""

1)List of screw types with number of units in stock and total value in stock
2)No. of units in stock in each length category
3)List of screws available sorted by length
4)Modify stock levels
5)Modify discounts
6)Bar chart displaying number of units in each length unit
7)Exit
""")
    option = input("Please enter an optionn \n")

    if option == "1":
        bF1(globalList)
        main()
    elif option == "2":
        bF2(globalList)
        main()
    elif option == "3":
        bF3(globalList)
        main()
    elif option == "4":
        bF4(globalList)
        main()
    elif option == "5":
        bF5(globalList)
        main()
    elif option == "6":
        barChart(globalList)
        main()
    elif option == "7":
        quit()
    elif option == "printlist":
        print(globalList)
        main()
    else:
        print("Invalid Option!")
        main()

if __name__ == "__main__":
    main()
    
