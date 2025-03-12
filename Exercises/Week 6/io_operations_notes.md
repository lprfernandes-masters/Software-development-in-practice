https://realpython.com/read-write-files-python/

// to open a file (defaults to read-only)

    with open("C:\\dogs.txt") as file:
        # Do something with the file

// to open a file with write rights

    with open("C:\\dogs.txt", "w") as file:

// to read a file

    with open("foo.txt", "r") as file:
        txt = file.read() //reads everything
        line = file.readline() //reads one line
        lines = file.readlines() //reads every line and returns a list

// to write

    with open("foo.txt", "w") as writer:
        writer.write("fizz")
        writer.writelines(lst)

// to open byte string files we suffix the option b

    with open("foo.png", "rb") as byte_reader:
