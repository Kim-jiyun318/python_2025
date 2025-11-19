import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "proverbs.txt")
infile = open(file_path, "r")

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()