import json
import os
from loan import Loan

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "loans.json")


class LoanRepository:
    def __init__(self):
        self.file_path = FILE_PATH
        self._ensure_storage()

    def _ensure_storage(self):
        directory = os.path.dirname(self.file_path)
        os.makedirs(directory, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump({"loans": []}, f, ensure_ascii=False, indent=2)

    def load_loans(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_loans(self, loans):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(loans, f, ensure_ascii=False, indent=2)

    def add_loan(self, loan: Loan):
        data = self.load_loans()

        data["loans"].append(loan.to_dict())
        self.save_loans(data)

    def remove_loan(self, user, book):
        data = self.load_loans()
        original_size = len(data["loans"])

        data["loans"] = [
            loan for loan in data["loans"]
                if not (loan["user"] == user and loan["book"] == book)
        ]
        
        if len(data["loans"]) == original_size:
            return False
          
        self.save_loans(data)  
        return 

    def list_loans(self):
        data = self.load_loans()
        return [Loan.from_dict(loan) for loan in data["loans"]]