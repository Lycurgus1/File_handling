# Creating class
class Text_file_handling:

    # Intialising class
    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # Reading to text
    def read_text_file(self):
        # Open file, have to specify what mode opening it in
        file = open(self.file_path, "r")
        # Read file. Number records amount of characters read
        file.tell() # Pointer is at current position and will start reading from there
        # file.seek(10) # Tells code where to print from
        self.text_storage = file.read(10)
        # Close file, returning variable so it is saved
        file.close()
        return self.text_storage

    # Writing to text
    def write_text_file(self):
        # Open file, have to specify what mode opening it in
        # Also specify file to be created
        file = open("writer.txt", "w")
        # Writing to file
        file.write("First python created file")
        # Close file, returning variable so it is saved
        file.close()

        # # Can use this to check file has close, and what mode you used
        # print(file.closed)
        # print(file.name)
        # print(file.mode)

        # # Opening file to append it. Use a not w
        # file = open("writer.txt", "a")
        # # Writing to file
        # file.write("\n append?")
        # # Close file, returning variable so it is saved
        # file.close()

        # # To append and read, use a+
        # file = open("writer.txt", "a+")
        # # Writing to file
        # file.write("\n appending")
        # # Reading from beginning, else file reads from after code inserted
        # file.seek(0)
        # self.text_storage = file.read()
        # # Close file, returning variable so it is saved
        # file.close()
        # return self.text_storage

        # # Open file, to overwrite file
        # file = open("writer.txt", "w")
        # # Writing to file
        # file.write("This is overriding")
        # # Close file, returning variable so it is saved
        # file.close()

    # Reading to text using with
    def read_text_file_with(self):
        # Reduce overhead of closing files
        # Opening the file and just read it.
        # Automatically closes it
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage

    # Writing to text using with
    def write_text_file_with(self):
        # with open("writer.txt", "w+") as file:
        #     file.write("Using writer with functionality")

        # Using append plus, to read and append
        with open("writer.txt", "a+") as file:
            file.write("\nUsing writer with functionality, append")
            # Need to included file.seek to repostion pointer
            file.seek(0)
            self.text_storage = file.read()
            return self.text_storage