# reading in txt files using with command
example1 = "C:\Dhruv\misc\data\python_for_data_science\wk4\example1.txt"

# using with to store and print contents
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# closes file automatically
print(file1.closed)

# stored data remains
print(FileContent)
