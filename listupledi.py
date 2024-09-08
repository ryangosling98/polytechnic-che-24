# Creating lists, tuples, and dictionaries
fruits = ["apple", "banana", "orange"]
numbers = (1, 2, 3, 4)
person = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing elements and performing operations
print("Fruits:", fruits)
print("Numbers:", numbers)
print("Person:", person)

fruits.append("grape")
print("Updated fruits:", fruits)

person["age"] = 31
print("Updated person:", person)

# Combining data structures
student_data = [
    {"name": "Bob", "age": 25, "grades": (90, 85, 92)},
    {"name": "Charlie", "age": 23, "grades": (88, 91, 87)}
]

print("Student data:", student_data)
print("First student's second grade:", student_data[0]["grades"][1])