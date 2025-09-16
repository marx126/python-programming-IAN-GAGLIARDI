# Test results

file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/08-file-handling-exercises/test_result.txt"

with open(file_path, "r") as f_read, open(file_path, "a") as f_append:
    print(f_read.read())
        