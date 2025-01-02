class Publisher:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Publisher:",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
    def display(self):
            super().display()
            print("Title:",self.title)
            print("Author:",self.author)
class Python(Book):
    def __init__(self,name,title,author,price,no_of_pages):
        super().__init__(name,title,author)
        self.price=price
        self.noofpages=noofpages
    def display(self):
        super().display()
        print("Price:",self.price)
        print("No Of Pages:",self.no_of_pages)
p=Python("DC BOOKS ","Oru Deshathinte Kadha","S.K.Pottekatt",639,565)
p.display()
