from loan import Loan
from repository import LoanRepository

class LoanService:
    def __init__(self, repo: LoanRepository):
        self.repo = repo

    def add_loan(self, user: str, book: str):
        loans = self.repo.list_loans()

        for loan in loans:
            if loan.user == user and loan.book == book:
                raise ValueError("This loan already exist.")
            
        loan = Loan(user, book)
        self.repo.add_loan(loan)

    def remove_loan(self, user: str, book: str):
        loans = self.repo.list_loans()

        for loan in loans:
            if loan.user == user and loan.book == book:
                self.repo.remove_loan(user, book)
                return
            
        raise ValueError("Loan not found.")
    
    def list_loans(self):
        return self.repo.list_loans()