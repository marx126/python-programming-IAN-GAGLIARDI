# Name cleaner

names = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "]
def clean_names(my_list: list):
    cleaned = []
    for name in my_list:
        cleaned.append(name.strip().title())
    return cleaned

for name in clean_names(names):
    print(name)