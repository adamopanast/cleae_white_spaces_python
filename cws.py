import sys
import re


fileName = sys.argv[1]
print('filename : `%s` ' %fileName)

linesCount = 0

output = open(fileName+'_FINAL','w+')

with open(fileName,'r') as fp:
    for line in fp:
        linesCount += 1
        line = re.sub(' ', '',line)
        output.write(line)
output.close()