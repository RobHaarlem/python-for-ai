# Sets only stores unique values

numbers= {1,2,4,3,2,4,5,6,54,8,9,8}
print(f"number-set: {numbers}")

colors={"red","green"}
# add item
colors.add("green")
print(colors)
colors.add("blue")
print(colors)
unique_numbers=list(set(numbers))
print(unique_numbers)
