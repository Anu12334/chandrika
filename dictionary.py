#x = ((a="chandrika",b="ajay",c="anusha"))

x = {"name":"chandrika","age":24,"branch":"bsc"}
print(x)

print(x["name"])# Access using key
print(x.get("age")) # Access using get()

x["age"] = 25 # Adding a new key-value pair

x[1] = "prakasam dist" # Updating an existing value
print(x)

del x["age"] # Using del to remove an item
print(x)

val = x.pop(1) # Using pop() to remove an item and return the value
print(val)

#Using popitem to removes and returns
key, val = x.popitem()  # the last key-value pair.
print(f"Key: {key}, Value: {val}")

x.clear()# Clear all items from the dictionary
print(x)