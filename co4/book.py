class publisher:
    def __init__(self,pubname):
        self.pubname=pubname
    def display(self):
        print("publisher name is:",self.pubname)
class Book(publisher):
    def __init__(self,pubname,title,author):
        publisher.__init__(self,pubname)
        self.title=title
        self.author=author
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
class python(Book):
    def __init__(self,pubname,title,author,price,no_of_pages):
        Book.__init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("price:",self.price)
        print("no_of_pages:",self.no_of_pages)
        
b1=python("D C BOOKS","WINGS OF FIRE","A P J Abdual kalam",100,325)
b1.display()
    
