class Rectangle:
    def __init__(self,l,w):
        self.__length=l
        self.__width=w
    def area(self):
        return self.__length*self.__width
    def __lt__(self, other):
        if self.area()<other.area():
            return True
        else:
            return False
r1=Rectangle(5,6)
r2=Rectangle(4,7)
if r1<r2:
    print("r1 is smaller")
else:
    print("r2 is smaller")