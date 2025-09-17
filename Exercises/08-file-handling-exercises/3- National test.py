# National test
import matplotlib.pyplot as plt

data_path_1 = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/08-file-handling-exercises/NPvt19Ma2A.txt"
data_path_2 = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/08-file-handling-exercises/NPvt19Ma2C.txt"

with open(data_path_1, "r") as f:
    data_1 = f.readlines()
    data_1 = [data.strip() for data in data_1]
    clean_data = []
    only_float_1 = []
    for data in data_1:
        clean_data.append(data[2:])
    for data in clean_data:
        only_float_1.append(float(data[:-1]))

# only_float_1 is a list that contains all cleaned data from data_path_1

with open(data_path_2, "r") as f:
    data_1 = f.readlines()
    data_1 = [data.strip() for data in data_1]
    clean_data = []
    only_float_2 = []
    for data in data_1:
        clean_data.append(data[2:])
    for data in clean_data:
        only_float_2.append(float(data[:-1]))

# only_float_2 is a list that contains all cleaned data from data_path_2

label = ["A", "B", "C", "D", "E", "F"]
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].pie(only_float_1, labels=label)
axes[0].set_title("NP Ma2A")

axes[1].pie(only_float_2, labels=label)
axes[1].set_title("NP Ma2C")

plt.show()