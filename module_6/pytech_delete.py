import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.cypjrxe.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

docs = collection.find()

print ("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

new_student = {
        "student_id": "1010",
        "first_name": "John",
        "last_name": "Smith"
    }

document_id = collection.insert_one(new_student).inserted_id

print("-- INSERT STATEMENTS --")
print(f"Inserted student record into student collection with document_id {document_id}")

print("--DISPLAYING STUDENT DOC")

doc = collection.find_one({"student_id": "1010"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")
print()

doc=collection.delete_one({"student_id": "1010"})

docs = collection.find()

print ("--DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

print("End of program, press any key to continue...")