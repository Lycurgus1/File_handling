# Python file handling
**General syntax**
- open method
```python
file_path = "order.txt"
text_file_object = Text_file_handling(file_path)
file = open(text_file_object, "r")
```
**Closing file**
- Can keep file open theoreticaly but,
- if so cannot open it elsewhere and there is limit to files you can have open
```python
file.close()
```
**Reading from text**
```python
    def read_text_file(self):
        # Open file, have to specify what mode opening it in
        file = open(self.file_path, "r")
        # Read file. Number records amount of characters read
        file.tell() # Pointer is at current position and will start reading from there
        self.text_storage = file.read(10)
        # Close file, returning variable so it is saved
        file.close()
        return self.text_storage
```

- file.readline, returns lines file and can have mutiple for more lines
```python
# Readline
file = open(file_path, "r")
# Prints out lines individual based on amoutn of readline methods
storage = file.readline()
storage2 = file.readline()
print(storage)
print(storage2)
```
- file.readlines, returns lines of file in list
```python
# Readlines
file = open(file_path, "r")
# Creates list of file with lines differeinated
storage = file.readlines()
print(storage)
```
- file. tell. Records where pointer is, can be used after writing to file
```python
# Read file. Number records amount of characters read
file.tell()  # Pointer is at current position and will start reading from there
```
- file.seek, tells code where to print from
```python
file.seek(10) 
```
**Writing from text**
- Write
```python
    def write_text_file(self):
        # Open file, have to specify what mode opening it in
        # Also specify file to be created
        file = open("writer.txt", "w")
        # Writing to file
        file.write("First python created file")
        # Close file, returning variable so it is saved
        file.close()
```
- Append
```python
    def write_text_file(self):
        # Open file, have to specify what mode opening it in
        # Also specify file to be created
        file = open("writer.txt", "a")
        # Writing to file
        file.write("First python created file")
        # Close file, returning variable so it is saved
        file.close()
```
- Write & append
    - need to includes file.seek(0)
    - else will read from after append
```python
        # To append and read, use a+
        file = open("writer.txt", "a+")
        # Writing to file
        file.write("\n appending")
        # Reading from beginning, else file reads from after code inserted
        file.seek(0)
        self.text_storage = file.read()
        # Close file, returning variable so it is saved
        file.close()
        return self.text_storage
```
- Checking file has closed
```python
        print(file.closed)
        print(file.name)
        print(file.mode)
```

**Reading from text using with**
- Enables closing and opening files automatically
```python
    def read_text_file_with(self):
        # Reduce overhead of closing files
        # Opening the file and just read it.
        # Automatically closes it
        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage
```
**Writing from text using with**
- Enables closing and opening files automatically
```python
    def write_text_file_with(self):
        # with open("writer.txt", "w+") as file:
        #     file.write("Using writer with functionality")
        # Using append plus, to read and append
        with open("writer.txt", "a+") as file:
            file.write("\nUsing writer with functionality, append")
            # Need to included file.seek to repostion pointer
            print(file.tell())
            file.seek(0)
            self.text_storage = file.read()
            return self.text_storage
```
**OSModule**
- Directory interaction
```python
# Get current working directory
        print(os.getcwd())
```
- list Directory
```python
print(os.listdir())
```
- Deleting file
```python
os.remove("writer.txt")
```
- Renaming file
```python
os.rename("order.txt", "modified.txt")
```
- Changing directory
```python
os.open("modified.txt", 5, 6)
```
- Making directory
```python
os.mkdir("Max")
```
- Removing directory
```python
os.rmdir("Max")
```