import os


def FindDuplicatesByDirectory(path):
    listOfFile = os.listdir(path)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + FindDuplicatesByDirectory(fullPath)
        else:
            allFiles.append(os.path.basename(fullPath))
    PrintList(allFiles)
    #seen_set = set()
    #duplicate_set = set(x for x in allFiles if x in seen_set or seen_set.add(x))
    #return list(duplicate_set)
    dupes = [item for n, item in enumerate(allFiles) if item in allFiles[:n]]
    return dupes


def PrintList(lst):
    for x in lst:
        print(x)


def main():
    path = input()
    PrintList(FindDuplicatesByDirectory(path))


if __name__ == "__main__":
    main()
