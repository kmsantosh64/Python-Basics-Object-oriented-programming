
# Campus Library Management System

## 1. Project Description

This project is a simple Campus Library Management System developed using Python and Object-Oriented Programming concepts.

The system manages three types of library items:
- Books
- Magazines
- DVDs

It allows library members to borrow and return items while checking item availability and borrowing limits.

The program also calculates late fees based on the type of item.

## 2. Project Structure

```text
library_manager/
│
├── models.py
├── main.py
├── output.txt
└── README.md
```

## 3. Features

- Uses an abstract parent class called `LibraryItem`.
- Implements separate classes for Book, Magazine and DVD.
- Uses inheritance to share common item behaviour.
- Calculates different late fees:
  - Book: Rs 2 per day
  - Magazine: Rs 1 per day
  - DVD: Rs 5 per day
- Maintains item availability.
- Stores each member's borrowed items privately.
- Enforces borrowing limits.
- Handles invalid borrowing and returning operations using `ValueError`.
- Demonstrates polymorphism through a common `late_fee()` method.
- Tracks the total number of library items.

## 4. How to Run

Python 3.12 or later is required.

Open a terminal inside the project folder and execute:

```bash
py main.py
```

To save the program output:

```powershell
py main.py > output.txt
```


