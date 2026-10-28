# Dictionaries
my_dict={}

person={
  "name": "Alice",
  "age":25,
  "city":"New York"
}
print(person["city"])
person["name"]="Rob"
person["gender"]="male"
person["licence"]=True
print(person)
del person["age"]
print(person)
print(person.keys())
print(person.values())
print(person.items())

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}
print(students["alice"]["grade"])