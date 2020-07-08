class Diff_text_file_handling:

    # Intialising class
    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage

    # Reading to text
    def read_text_file(self):
        # Tries try statement. If works run else
        # Put code you think will raise exception
        try:
            file = open(self.file_path, "r")
        # Except runs if error occurs
        # If certain error occurs can do specific thing
        except NameError:
            print("Variable file is not defined")
        # Catches thrown exception
        except Exception as e:
            print(e)
        # Runs if try statement succeeds(if no exception)
        else:
            file.tell()
            self.text_storage = file.read(10)
            file.close()
            return self.text_storage
        # Will always run, irrelevant of exception
        # Mandatory code
        finally:
            print("this will always run")

