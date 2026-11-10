
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

## 5. Reflection Questions

### Question 1: Why is LibraryItem an abstract class? What happens if DVD does not implement late_fee()?

`LibraryItem` is an abstract class because it provides common properties and methods that all library items should share. It also defines the abstract method `late_fee()`, which requires every child class to implement its own late fee calculation.

If DVD does not implement `late_fee()`, Python will not allow us to create a DVD object because it has not implemented all the required abstract methods.

### Question 2: What happens if we try to access item.__available outside the class? Why do we use is_available()?

Trying to access `item.__available` outside the class raises an `AttributeError` because the attribute is private and Python applies name mangling to it.

We use the `is_available()` method to check the item's availability safely without accessing the private attribute directly. This demonstrates encapsulation.

### Question 3: What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the LibraryItem class and its child classes. It stores the total number of library items created.

`self.title` is an instance attribute. Each individual item object has its own title, which can be different from the titles of other objects.
