import os

def count_words():
    filename = input("Enter the file name: ")

    if os.path.exists(filename) == False:
        print("File not found.")
        return

    file = open(filename, "r")
    contents = file.read()
    file.close()

    words = contents.split()
    word_count = len(words)

    print("Total words: " + str(word_count))

count_words()
