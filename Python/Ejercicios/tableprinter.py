tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"]]

def printtable(list):
    newTable = [[] for x in range(len(list[0]))]

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            newTable[j].append(list[i][j])


    maximaAnchura = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (len(list[i][j]) > maximaAnchura):
                maximaAnchura = len(list[i][j])

    for row in newTable:
        print("\n")
        for j in range(0,len(row)):
            print(row[j].rjust(maximaAnchura), end=" ")

printtable(tableData)
