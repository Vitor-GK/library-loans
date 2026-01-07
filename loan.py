class Loan:
    def __init__(self, user: str, book: str):
        if not user or not book:
            raise ValueError("User and book are required.")
        self.user = user
        self.book = book

    def __str__(self):
        return f"user = {self.user}, book = {self.book};" 
    
    def to_dict(self):
        return {"user": self.user, "book": self.book}
    
    @staticmethod
    def from_dict(data):
        return Loan(data["user"], data["book"])