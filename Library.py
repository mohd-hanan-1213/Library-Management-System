from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["library_dbteat"]

books = db["books"]
members = db["members"]
issued = db["issued_books"]
categories = db["categories"]
transactions = db["transactions"]

while True:

    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Member")
    print("4. View Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Add Category")
    print("8. View Categories with Books")
    print("9. View Transactions")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        book_id = int(input("Book ID: "))

        if books.find_one({"book_id": book_id}):
            print("Book ID already exists!")
            continue

        title = input("Title: ")
        author = input("Author: ")

        category_id = int(input("Category ID: "))
        category = categories.find_one({"category_id": category_id})

        if not category:
            print("Category not found!")
            continue

        copies = int(input("Copies: "))

        books.insert_one({
            "book_id": book_id,
            "title": title,
            "author": author,
            "category_id": category_id,
            "copies": copies
        })

        print("Book added successfully")

    elif choice == 2:

        print("\nBooks:\n")

        for b in books.find():
            cat = categories.find_one({"category_id": b["category_id"]})
            cname = cat["name"] if cat else "N/A"

            print(f"ID: {b['book_id']} | {b['title']} | Author: {b['author']} | Category: {cname} | Copies: {b['copies']}")


    elif choice == 3:

        member_id = int(input("Member ID: "))

        if members.find_one({"member_id": member_id}):
            print("Member already exists!")
            continue

        name = input("Name: ")
        phone = input("Phone: ")

        members.insert_one({
            "member_id": member_id,
            "name": name,
            "phone": phone
        })

        print("Member added successfully")


    elif choice == 4:

        print("\nMembers:\n")

        for m in members.find():
            print(f"ID: {m['member_id']} | Name: {m['name']} | Phone: {m['phone']}")

    elif choice == 5:

        book_id = int(input("Book ID: "))
        member_id = int(input("Member ID: "))

        book = books.find_one({"book_id": book_id})
        member = members.find_one({"member_id": member_id})

        if not book:
            print("Book not found!")
            continue

        if not member:
            print("Member not found!")
            continue

        if book["copies"] <= 0:
            print("No copies available!")
            continue

        if issued.find_one({"book_id": book_id, "member_id": member_id}):
            print("Book already issued to this member!")
            continue

        issued.insert_one({
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": datetime.now()
        })

        books.update_one({"book_id": book_id}, {"$inc": {"copies": -1}})

        transactions.insert_one({
            "book_id": book_id,
            "member_id": member_id,
            "type": "ISSUE",
            "date": datetime.now()
        })

        print("Book issued successfully")

    elif choice == 6:

        book_id = int(input("Book ID: "))
        member_id = int(input("Member ID: "))

        result = issued.delete_one({
            "book_id": book_id,
            "member_id": member_id
        })

        if result.deleted_count == 0:
            print("No such issued record!")
        else:
            books.update_one({"book_id": book_id}, {"$inc": {"copies": 1}})

            transactions.insert_one({
                "book_id": book_id,
                "member_id": member_id,
                "type": "RETURN",
                "date": datetime.now()
            })

            print("Book returned successfully")

    
    elif choice == 7:

        category_id = int(input("Category ID: "))
        name = input("Category Name: ")

        if categories.find_one({"category_id": category_id}):
            print("Category already exists!")
            continue

        categories.insert_one({
            "category_id": category_id,
            "name": name
        })

        print("Category added successfully")


    elif choice == 8:

        print("\nCategories with Books:\n")

        for c in categories.find():

            print(f"\nCategory: {c['name']} (ID: {c['category_id']})")
            print("-" * 40)

            books_in_category = books.find({"category_id": c["category_id"]})

            found = False
            for b in books_in_category:
                print(f"Book ID: {b['book_id']} | {b['title']} | Copies: {b['copies']}")
                found = True

            if not found:
                print("No books in this category")


    elif choice == 9:

        print("\nTransactions:\n")

        for t in transactions.find():
            print(f"Book: {t['book_id']} | Member: {t['member_id']} | {t['type']} | {t['date']}")


    elif choice == 10:
        print("Exiting...")
        break

    else:
        print("Invalid choice")