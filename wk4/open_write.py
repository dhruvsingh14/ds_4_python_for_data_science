#################################
# writing text files using open #
#################################
with open("example2.txt", "w") as File1:
    File1.write("This is line A\n")
    File1.write("This is line B\n")

# keep in mind that \n is a line break
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# using for loop to write lines out to  a text file
with open("example2.txt", "w") as File1:
    for line in Lines:
        File1.write(line)

# can set mode to appended to write to the existing file without overwriting
with open("example2.txt", "a") as File1:
    File1.write("This is line C")
