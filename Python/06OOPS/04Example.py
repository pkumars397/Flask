class Book:
    Types=["hardcover","paperback"]
    def __init__(self,name,book_type,weight):
        self.name=name
        self.bookType=book_type
        self.weight=weight

    def __repr__(self):
        return f"<Book {self.name} {self.bookType} weighting {self.weight}>"
    
    @classmethod
    def hardcover(cls,name,page_weight):
        return cls(name,cls.Types[0],page_weight+100)
    
    @classmethod
    def paperBack(cls,name,pageWeight):
        return cls(name,cls.Types[1],pageWeight)

book=Book("Harry Potter","Hardcover",2000)
print(book)

#but we want to create the book of only two type hardcover or paperback
book1=Book.hardcover("Harry",1500)
light=Book.paperBack("Python",600)
print(book1,light,end="\n")