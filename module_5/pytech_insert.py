import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.cypjrxe.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
records = [
    {
        "student_id": "1007",
        "first_name": "Thorin",
        "last_name": "Oakenshield II"
    },
    {
        "student_id": "1008",
        "first_name": "Bilbo",
        "last_name": "Baggins",
    },
    {
        "student_id": "1009",
        "first_name": "Frodo",
        "last_name": "Baggins",
    }
]

print("-- INSERT STATEMENTS --")
for record in records:
    new_student_id = collection.insert_one(record).inserted_id
    print(f"Inserted student record {record['first_name']} {record['last_name']} into student collection with document_id {new_student_id}")
print()
print("End of program, press any key to continue...")


