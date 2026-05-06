#flie handling in python

with open("test.txt", "w") as f:
    f.write("My name is Smarika")
    f.write("I am learning Python")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)


#f.write() simple concatenate sentences without new line character

with open("test.txt", "w") as f:
    f.write("My name is Smarika\n")
    f.write("I am learning Python")

with open("test.txt", "r") as f:
    content = f.read()
    print(content)


#Task-1

with open("log.txt", "w") as f:
    f.write("App started\n")

with open("log.txt", "a") as f:
    f.write("User logged in\n")
    f.write("User logged out\n")

with open("log.txt", "r") as f:
    content = f.read()
    print(content)
