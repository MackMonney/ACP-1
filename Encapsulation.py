#class square
class square:

    def __init__(self):
        #private attribute
        self.__side = 10

    def area(self):
        print("side :", self.__side)
        print("My area is :", self.__side**2)

ob = square()
#updating value of private attribute
ob.__side = 15
#calling area method to check the changes
ob.area()