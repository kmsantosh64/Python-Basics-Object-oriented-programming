
from models import Book, Magazine, DVD, Member, LibraryItem


# 1. Create library items
book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Science Today", 2, 45)
dvd = DVD("Inception", 3, 148)


# 2. Create library members
alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


# 3. Demonstrate borrowing
print("===== BORROWING ITEMS =====")

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)


# Bob tries to borrow an already borrowed book
try:
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)


# Bob borrows a magazine
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
except ValueError as e:
    print("Could not borrow:", e)


# Bob tries to exceed his borrowing limit
try:
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)


# 4. Demonstrate returning items
print("\n===== RETURNING ITEMS =====")

# Bob tries to return a book he never borrowed
try:
    bob.return_item(book)
except ValueError as e:
    print("Could not return:", e)


# Alice returns her book after 3 late days
try:
    fee = alice.return_item(book, 3)
    print("Alice returned:", book.title)
    print("Late fee: Rs", fee)
except ValueError as e:
    print("Could not return:", e)


# 5. Demonstrate polymorphism
print("\n===== ITEM LATE FEES =====")

items = [book, magazine, dvd]

for item in items:
    print(
        item.describe(),
        "-> Late fee for 3 days: Rs",
        item.late_fee(3)
    )


# 6. Display borrowed items
print("\n===== MEMBER BORROWING DETAILS =====")

print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())


# 7. Display total number of library items
print("\n===== LIBRARY DETAILS =====")

print("Total library items:", LibraryItem.total_items)



