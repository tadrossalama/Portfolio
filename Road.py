'''
Program to calculate the ammount of asphalt need, (in cubic feet) to pave a road at a given thickness.
1. receives the width (ft)
2. length (miles)
3. thickness needed (inch)
The methods will be converting all dimensions into feet
 and calculate the cubic feet by:
 setHeight(ft) x setWidth(ht) x asphalt_needed(n * 12) = Cubic feet needed 
'''

class Road:
    def __init__(self):
        self.__width = 0
        self.__length = 0 #length in miles, (as inputed)
        self.length_in_ft = 0 #length converted to feet
        self.__asphalt_needed = 0
    #Mutators
    ##Width (ft)
    def setWidth(self, width):
        self.__width = width
    
    ##Length (miles)
    ###`miles_to_feet`: Convert miles to feet
    def setLength(self, length):
        miles_to_feet = 5280
        self.__length = length 
        self.length_in_ft = length * miles_to_feet
    
    #Access
    def getWidth(self):
        return self.__width
    def getLength(self):
        return self.__length
    
    ##thickness needed entered in inches
    ###convert inches to ft using `inch_to_ft` 
    def asphalt_needed(self, thickness):
        inch_to_feet = 12
        self.thickness = thickness / inch_to_feet
        self.__asphalt_needed = self.length_in_ft * self.__width * self.thickness
        return(self.__asphalt_needed)

         




def driver():
    road = Road()
    print(road)

if __name__ == '__main__':
    driver()
