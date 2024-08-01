list = ['apples', 'bananas', 'tofu', 'cats']
list.insert(-1, 'and')
for i in range(0, len(list)):
    print(f"{list[i]}", end=", ")
