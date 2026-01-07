# Library Loan System

A simple Python command-line system for managing book loans in a library.  
It allows users to register, remove, and list active loans with data persistence using JSON.

## Features

- Add new book loans
- Remove existing loans
- List all active loans
- Persist loan data using JSON files
- Prevent duplicate loan records

## Project Structure

library-loans/
├── cli.py            # Command-line interface
├── loan.py           # Loan domain model
├── loanservice.py    # Business logic layer
├── repository.py     # Data persistence layer (JSON)
├── data/
│   └── loans.json    # Stored loan records
└── README.md

## Technologies Used

- Python 3
- JSON for data persistence
- Standard Python libraries (`os`, `json`)


## How to Run

```bash
git clone https://github.com/Vitor-GK/library-loans.git
cd library-loans
python cli.py


## System Architecture

The application follows a layered architecture to separate responsibilities and improve maintainability:

- **CLI Layer (`cli.py`)**  
  Handles user interaction and input/output via the command line.

- **Service Layer (`loanservice.py`)**  
  Contains business rules and validations, such as preventing duplicate loans.

- **Repository Layer (`repository.py`)**  
  Manages data persistence using JSON files and abstracts file operations.

- **Domain Model (`loan.py`)**  
  Represents the core entity of the system: a library loan.

## Future Improvements

- Support for due dates and loan return tracking
- Unique identifiers for users and books
- Improved error handling and user feedback
- Migration from JSON storage to a relational database
- Unit tests for service and repository layers

## Author

Developed by **Vitor Glier Kockhann**  
GitHub: https://github.com/Vitor-GK
LinkedIn: https://www.linkedin.com/in/vitor-glier-kockhann-956a9b353/ 