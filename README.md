# 📚 Library Management System

### MongoDB + Python CLI Application

A robust command-line based Library Management System designed to demonstrate practical database operations using **Python** and **MongoDB**. This project simulates real-world library workflows including book tracking, member management, and transaction logging.

---

## 🚀 Overview

This application provides a structured system to manage:

* 📖 Books inventory
* 👤 Library members
* 🏷️ Categories
* 🔄 Book issue/return operations
* 📊 Transaction history

It uses **MongoDB (NoSQL)** for flexible data storage and **PyMongo** for seamless database interaction.

---

## 🧠 Key Highlights

* ✔️ Clean CLI-based interaction model
* ✔️ Efficient use of MongoDB collections
* ✔️ Data validation (duplicate checks, availability checks)
* ✔️ Transaction logging system
* ✔️ Modular and scalable database design

---

## 🛠️ Tech Stack

| Technology | Purpose                |
| ---------- | ---------------------- |
| Python     | Core application logic |
| MongoDB    | Database               |
| PyMongo    | Database connectivity  |

---

## 🏗️ System Architecture

The application uses multiple collections to maintain data integrity and separation of concerns:

```
library_db
│
├── books
├── members
├── categories
├── issued_books
└── transactions
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
```

---

### 2️⃣ Install Dependencies

```bash
pip install pymongo
```

---

### 3️⃣ Start MongoDB

Ensure MongoDB is running locally:

```
mongodb://localhost:27017/
```

---

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 🧩 Features Breakdown

### 📖 Book Management

* Add new books with category mapping
* View all books with category details
* Tracks available copies

---

### 👤 Member Management

* Register new members
* View member details

---

### 🏷️ Category Management

* Add and manage book categories
* View categories with associated books

---

### 🔄 Issue & Return System

* Issue books with validation checks
* Prevent duplicate issue entries
* Return books and update inventory

---

### 📊 Transaction Tracking

* Logs every issue and return action
* Maintains timestamped records

---

## 🔄 Workflow Example

1. Add Category
2. Add Book under Category
3. Register Member
4. Issue Book
5. Return Book
6. View Transaction Logs

---

## 📌 Sample Document (Book)

```json
{
  "book_id": 101,
  "title": "Data Structures",
  "author": "Author Name",
  "category_id": 1,
  "copies": 3
}
```

---

## ⚠️ Design Considerations

* Unique IDs enforced for books and members
* Category must exist before assigning to a book
* Copies are updated atomically using MongoDB operators
* Transactions stored separately for auditability

---

## 📈 Learning Outcomes

This project demonstrates:

* NoSQL database design principles
* CRUD operations with MongoDB
* Data consistency handling
* Real-world system workflow modeling
* Backend logic structuring in Python

---

## ⭐ Support

If you found this project useful:

* ⭐ I you found this project useful, please give it a star on GitHub!
* 📝 Feel free to contribute or suggest improvements.


---
