# Test results
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/08-file-handling-exercises/test_result.txt"

with open(file_path, "r") as f_read:
    lines = f_read.readlines()

lines = [line.strip() for line in lines]
lines.sort()

with open(file_path, "a") as f_append:
    f_append.write("\n")
    f_append.write(f"\nSorted alphabetically:\n")
    f_append.write("\n")
    for line in lines:
        f_append.write(line + "\n")

a = []
b = []
c = []
d = []
e = []
f = []
for i in lines:
    if int(i[-2:]) < 20:
        f.append(i)
    elif int(i[-2:]) < 30:
        e.append(i)
    elif int(i[-2:]) < 40:
        d.append(i)
    elif int(i[-2:]) < 50:
        c.append(i)
    elif int(i[-2:]) < 60:
        b.append(i)
    elif int(i[-2:]) < 70:
        a.append(i)

with open(file_path, "a") as f_append:
    f_append.write(f"\nSorted results:\n")
    f_append.write("\n")

    f_append.write(f"Grade: A\n")
    for i in a:
        f_append.write(i + "\n")
    
    f_append.write(f"Grade: B\n")
    for i in b:
        f_append.write(i + "\n")

    f_append.write(f"Grade: C\n")
    for i in c:
        f_append.write(i + "\n")

    f_append.write(f"Grade: D\n")
    for i in d:
        f_append.write(i + "\n")

    f_append.write(f"Grade: E\n")
    for i in e:
        f_append.write(i + "\n")

    f_append.write(f"Grade: F\n")
    for i in f:
        f_append.write(i + "\n")

# Not my proudest code but it works