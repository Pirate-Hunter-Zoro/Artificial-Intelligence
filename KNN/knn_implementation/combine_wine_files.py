import os

# Source: https://stackoverflow.com/questions/21957131/python-not-finding-file-in-the-same-directory
here = os.path.dirname(os.path.abspath(__file__))
filename_red = os.path.join(here, 'winequality-red.csv')
filename_white = os.path.join(here, 'winequality-white.csv')
filename_wine = os.path.join(here, 'winequality.csv')

f = open(filename_red, "r")
lines_red = f.readlines()
f.close()

f = open(filename_white, "r")
lines_white = f.readlines()
f.close()

f = open(filename_wine, "w")
f.write(lines_red[0][:-1] + "\"id\";\"type\"\n")
for i, line in enumerate(lines_red[1:]):
    f.write(line[:-1] + f';{i}' + ';0' + '\n')
for i, line in enumerate(lines_white[1:]):
    f.write(line[:-1] + f';{i + len(lines_red)-1}' + ';1' + '\n')
f.close()