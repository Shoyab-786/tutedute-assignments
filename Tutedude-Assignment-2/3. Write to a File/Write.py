# Open (or create) a file in write mode
file = open("example.txt", "w")

# Content to write
content = "Hello, this is some sample content written to the file.\nWelcome to file handling in Python."

# Write content to the file
file.write(content)

# Close the file
file.close()

print("Content written to example.txt successfully.")
