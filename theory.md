# Python file handling
**General syntax**
- open method

**Closing file**
- Can keep file open theoreticaly but,
- if so cannot open it elsewhere and there is limit to files you can have open

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

- file.readline
```python
# Readline
file = open(file_path, "r")
# Prints out lines individual based on amoutn of readline methods
storage = file.readline()
storage2 = file.readline()
print(storage)
print(storage2)
```
- file.readlines
```python
# Readlines
file = open(file_path, "r")
# Creates list of file with lines differeinated
storage = file.readlines()
print(storage)
```
- file. tell

- file.seek, tells code where to print from
```python
file.seek(10) 
```
**Writing from text**
- Write
- Append
- Write & append
    - need to includes file.seek(0)
    - else will read from after append
- Checking file has closed
- Writing and reading

**Reading from text using with**
- Enables closing and opening files automatically

**Writing from text using with**