class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value

    def contracts(self):
        """Returns a list of contracts for this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Returns a list of books the author has contracts for."""
        return list(set(contract.book for contract in self.contracts()))  # Use set to avoid duplicates

    def sign_contract(self, book, date, royalties):
        """Creates and returns a new Contract."""
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Calculates the total royalties the author has earned."""
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []  # Class variable to track all books

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value

    def contracts(self):
        """Returns a list of contracts for this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Returns a list of authors who have contracts for this book."""
        return list(set(contract.author for contract in self.contracts()))  # Avoid duplicates

class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns all contracts that have the same date as the given date."""
        return [contract for contract in cls.all_contracts if contract.date == date]
  
