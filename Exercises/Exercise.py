# Accept user input for some text.
# Ensure user enters something else raise an exception.
# After that write that text to a file and then
# read from this file to  write to another file simultaneously

# Importing image modules
import numpy
import cv2

# Creating class
class First_exercise:

    # Intialising class
    def __init__(self):
        pass

    # Method to get name and return it. Contains exception testing
    def user_input(self):
        # While true keeps loop going until satisfied
        while True:
            # Tests if name satisfies condition of having characters
            try:
                # Getting user input
                self.name = input("Enter name here\n")
                # Getting the name length is not enough characters, raise exception
                if len(self.name) <= 0:
                    raise Exception
            # Returns this if Exception hit
            except Exception:
                print("We do not accept empty names")
            # Returns if name has 1 characteror more
            else:
                # Prints name and ends while loop with return
                print("Thank you for entering your name")
                return self.name

    # Function to write name
    def write_name(self):
        # Calling previous function to get self.name
        self.user_input()
        # Using with open to write new file with previous name
        with open ("name.txt", "w+") as file:
            file.write(self.name)
            # Resetting cursor to read from beginning of file
            file.seek(0)
            self.new_text = str(file.read())

    # function to write another file
    def write_again(self):
        # Calling previous function to make sure have information before
        self.write_name()
        # using with to write new file with old text
        with open("new_file.text", "w+") as file:
            file.write(self.new_text)

    def upload_image(self):
        # Reading and showing image
        img = cv2.imread("leapord.jpg", 0)
        cv2.imshow("image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # Writing image
        cv2.imwrite("image.png", img)

# Calling function
obj1 = First_exercise()
# obj1.write_again()
obj1.upload_image()