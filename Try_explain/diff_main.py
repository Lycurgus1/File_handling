from diff_text_file import Diff_text_file_handling

# # Stating methods to get class object and file path sorted
file_path = "diff_modified.txt"
text_file_object = Diff_text_file_handling(file_path)
#
# # Calling/testing read text function
# print(text_file_object.read_text_file())

# # Raise an exception with if loop
# x = 6
#
# # If this is true, raise exception
# if x < 0:
#     raise Exception("No numbers below zero")
# else:
#     print(x)

# # Raising specific errors with if loop
# x = "test"
#
# # If loop with type specifiers
# if type(x) is not int: # If type(x) is str also possible
#     raise TypeError("Only strings allowed")

def raiseException():
    while True:
        try:
            first_value = input("Enter name here\n")
            if len(first_value) <= 0:
                raise Exception
        except Exception:
            print("We do not accept empty names")
        else:
            print("Thank you for entering your name")
            return first_value

raiseException()