class Book:
    def __init__(self,title:str,author:str,price:float,quantity:int):
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity
    def apply_discount(self,discount_percentage:int):
        return self.price*(1-discount_percentage/100)
    def sell(self,amount):
        if self>=amount:
            return self-amount
        else:
            return "not enough books"
    def __str__(self):
        return f"Назва {self.title}\tАвтор: {self.author}\tЦіна: {self.price}\tКількість: {self.quantity}"
class BookStore:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books
    def add_book(self,book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                b.quantity += book.quantity
                return f"Book '{book.title}' updated with {book.quantity} more copies."
        self.books.append(book)
        return f"Book '{book.title}' added to the store."
    def search(self,query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                results.append(book)
        if results:
            return results
        else:
            return "No books found matching the query."
    def calculate_total_value(self):
        suma=0
        for book in self.books:
            suma+=book.price * book.quantity
        return f"\nTotal value of all books in store: ${suma}"