class trinagle:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

class Triangle_Utilities(trinagle):
     def __init__(self,side1,side2,side3):
         trinagle.__init__(self,side1,side2,side3)
     
     def get_area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        print (str(s))
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

instance = Triangle_Utilities(3,4,5)
print ("Area of triangle = " + str(instance.get_area()) )


