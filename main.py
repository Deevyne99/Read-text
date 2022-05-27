# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from fileinput import filename


def read_file_content(filename):
    # [assignment] Add your code here
    filename = "story.txt"
    file = open(filename, "r")

    for x in file:
        print(x)
    # return "Hello World"


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = open("story.txt", "r")
# creating a dictionary
    d = dict()
    # then loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])


read_file_content(filename)
count_words()
