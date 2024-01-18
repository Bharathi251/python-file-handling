import os

# Open a File on the Server
f = open("demofile.txt", "r")
print(f.read())

# Open a file on a different location:
f = open("C:\\Users\\BharathiR\\Desktop\\demo.txt", "r")
print(f.read())

# Read Only Parts of the File
f = open("demofile.txt", "r")
print(f.read(5))

# Read Lines
f = open("demofile.txt", "r")
print(f.readline())

# By calling readline() two times, you can read the two first lines:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
    print(x)

# Close Files

f = open("demofile.txt", "r")
print(f.read())
f.close()

# Python File Write

# Open the file "demofile.txt" and append content to the file:

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
print(f.read())

# Open the file "demofile3.txt" and overwrite the content:
# the "w" method will overwrite the entire file.
f = open("demofile1.txt", "w")
f.write("whoops, its all deleted")
f.close()

f = open("demofile1.txt")
print(f.read())

# Create a new file
# "x" - Create - will create a file, returns an error if the file exist

# f = open("demofile3.txt", "x")

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:


# os.remove("myfile.txt")

# Check if File exist:

if os.path.exists("myfile2.txt"):
    os.remove("myfile2.txt")
else:
    print("The file does not exist")

# Delete Folder

os.rmdir("python")