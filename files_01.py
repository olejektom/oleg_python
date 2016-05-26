import sys
if len(sys.argv)<1:
    reader = sys.stdin
    sys.stdout = reader
for i in range (1, (len(sys.argv))):
    file_name = sys.argv[i]
    fhand = open (file_name, 'r')
    reader = fhand.read
    sys.stdout.write(reader)
print sys.stdout
