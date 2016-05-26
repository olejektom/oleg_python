import sys
file_name = sys.argv[1]
f = open(file_name, 'w')
x = sys.stdin.read()
f.write(x)
#the last part is not clear
