with open("file.txt", "r") as f:
    for word in f.read().split():
        print(word)
