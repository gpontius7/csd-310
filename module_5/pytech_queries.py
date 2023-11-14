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

print ("--DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")

doc = collection.find_one({"student_id": "1009"})

print(f"Student ID: {doc['student_id']}")
print(f"First Name: {doc['first_name']}")
print(f"Last Name: {doc['last_name']}")

print("End of program, press any key to continue...")


