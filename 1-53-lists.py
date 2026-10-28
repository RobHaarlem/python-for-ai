# Empty List
my_list=[]

# List with Items
fruits = ["apple","bananna","orange"]
numbers=[1,2,3,4,5]
mixed=["hello",42,True,3.14]

# Get Items
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

# Slicing
print(fruits[1:3])

# Change Lists
fruits[0]="mango"
print(fruits)
# Add Item
fruits.remove("bananna") # Remove by value
print(fruits)
last= fruits.pop()
print(f"last: {last}")
print(fruits)

fruits.append("apple")
fruits.append("bananna")
print(fruits)
fruits.insert(1,"bananna")
print(f"insert: {fruits}")

if "apple" in fruits:
  print(f"Found apple")

if fruits:
  print("List has items")
else:
  print("List has no items")

print(numbers.index(3))