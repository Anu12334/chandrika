# Create and write to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("This is the second line.")

# Read the file
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading file content:\n", content)

# Append to the file
with open("example.txt", "a") as file:
    file.write("\nThis line is added using append mode.")

# Read again after appending
with open("example.txt", "r") as file:
    content = file.read()
    print("\nReading file content after appending:\n", content)
