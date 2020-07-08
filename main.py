from text_file import Text_file_handling

# Reading from and writing to files
# Exception handling
# CSV
# Assignments

# Stating methods to get class object and file path sorted
file_path = "order.txt"
text_file_object = Text_file_handling(file_path)

# # Calling/testing read text function
# print(text_file_object.read_text_file())

# # Calling write text method, creating new text file
# text_file_object.write_text_file()

# # Testing append plus method
# print(text_file_object.write_text_file())

# # Testing read using with method
# print(text_file_object.read_text_file_with())

# Testing write using with method
print(text_file_object.write_text_file_with())

# # Readline
# file = open(file_path, "r")
# # Creates list of file with lines differeinated
# storage = file.readlines()
# # Prints out lines individual based on amoutn of readline methods
# storage = file.readline()
# storage2 = file.readline()
# print(storage)
# print(storage2)



# # Messing about
# file = open(file_path, "r")
# storage = file.tell()
# print(storage)
# x = []
# for char in storage:
#     x.append(char)
# print(x)
# for line in file:
#     print(line)

