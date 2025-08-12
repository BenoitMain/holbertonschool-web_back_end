<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

---

📦 NoSQL Project – Holberton School
📖 Overview
Welcome to the NoSQL adventure!
In this project, you’ll dive into MongoDB and the fundamentals of NoSQL databases through:

Mongo Shell – command-line operations

PyMongo – the official Python driver for MongoDB

You’ll learn how to work with document-oriented databases, run queries, and manage data in a flexible NoSQL environment.

🎯 Goals
By the end of this project, you will be able to:

Understand what NoSQL is and how it differs from traditional SQL

Use MongoDB both in the shell and with Python

Perform CRUD operations (Create, Read, Update, Delete)

Apply simple filters and aggregations

Bridge the gap between raw database commands and Python scripts

⚙️ Installation Guide
1️⃣ Installing MongoDB (Ubuntu 20.04+)
bash
Copier
Modifier
sudo apt update
sudo apt install -y mongodb
sudo systemctl start mongodb
sudo systemctl enable mongodb
💡 You can check if MongoDB is running with:

bash
Copier
Modifier
sudo systemctl status mongodb
2️⃣ Installing PyMongo
bash
Copier
Modifier
pip install pymongo
📂 Project Structure
pgsql
Copier
Modifier
NoSQL/
│── 0-list_databases              # List all databases
│── 1-use_or_create_database      # Use or create a database
│── 2-insert                      # Insert a document
│── 3-all                         # List all documents
│── 4-match                       # Filter by name
│── 5-count                       # Count documents
│── 6-update                      # Update a field
│── 7-delete                      # Delete a document
│── 8-all.py                      # Python: List all documents
│── 9-insert_school.py            # Python: Insert a document
│── 10-update_topics.py           # Python: Update topics
│── 11-schools_by_topic.py        # Python: Filter by topic
│── 12-log_stats.py               # Python: Analyze Nginx logs
│── README.md
🚀 Usage
Run Mongo Shell scripts:
bash
Copier
Modifier
cat 0-list_databases | mongo
Run Python scripts:
bash
Copier
Modifier
python3 8-main.py
📜 Task Highlights
0-list_databases → List all available databases

1-use_or_create_database → Switch to or create a database

2-insert → Insert a new document

3-all → Retrieve all documents

4-match → Filter results by name

5-count → Count the number of documents in a collection

6-update → Update an existing document field

7-delete → Remove a document

8-all.py → Python version of listing all documents

9-insert_school.py → Insert a new school document (Python)

10-update_topics.py → Update topics in a school document (Python)

11-schools_by_topic.py → Find schools by topic (Python)

12-log_stats.py → Process and analyze Nginx log data

💡 Tips for Success
Use mongosh instead of the older mongo shell for a better experience.

Always double-check your MongoDB connection string when using Python scripts.

Test your queries in the shell before adding them to Python for fewer debugging headaches.

📚 Resources
📖 MongoDB Documentation

🐍 PyMongo Documentation

💡 MongoDB Aggregation Pipeline
