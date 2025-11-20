import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "phones.txt")
infile = open(file_path, "r", encoding="utf-8") #원래 encoding이 없었다. 안하니까 한글출력이 안됨.
                                                #인코딩을 하니까 한글이 출력된다!
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()