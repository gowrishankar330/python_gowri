class book:
    def __init__(self, name , author, prize):
        self.name = name
        self.author = author
        self.prize = prize

    def __str__(self):
        return f"{self.name} is written by {self.author} & it costs {self.prize}"
    
    def __eq__(self, other):
        return self.name == other.name and self.author == other.author
    
    def __lt__(self, other):
        return self.prize < other.prize
    
    def __gt__(self, other):
        return self.prize > other.prize
    
    def __add__(self, other):
        return self.prize + other.prize
    
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.author
    
    def __getitem__(self, key):
        if key == "name":
         return self.name
        elif key == "author":
            return self.author
        else:
            return None

book1 = book("holymoly", "harish", 200)
book2 = book("holydoly", "darsan", 400)
book3 = book("holykoly", "sasi", 700)
book4 = book("holymoly", "gowri", 900)
book5 = book("food", "harish", 10)


print(book1)
print(book1 == book4)
print(book1 == book5)
print(book1 < book4)
print(book4 < book2)
print(book3 > book5)
print(book1 > book3)
print(book4 + book2)
print(book3 + book5)
print(book1 + book3)
print("holymoly" in book1)
print("gowri" in book4)
print("gomma" in book2)
print(book2['name'])
print(book4['author'])