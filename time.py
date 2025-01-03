class Time:
    def __init__(self,h,m,s):
        self. __hr=h
        self. __min=m
        self. __sec=s
    def __add__(self,other):
        h=self.__hr+other.__hr
        m=self.__min+other.__min
        s=self.__sec+other.__sec
        if s>60:
            m=m+int(s/60)
            s=s%60
        if m>60:
            h=h+int(m/60)
            m=m%60
        t3=Time(h,m,s)
        return t3
    def display(self):
        print(self.__hr)
        print(self.__min)
        print(self.__sec)
t1=Time(3,50,55)
t2=Time(5,16,56)
t3=t1+t2
t3.display()
