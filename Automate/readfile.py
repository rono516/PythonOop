f = open('inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
failFile = open('failFile.txt', 'w')

count = 0
for line in f:
    #split using white spaces
    line_split= line.split()
    if line_split[2] == 'P':
        print(line)
        passFile.write(line)
    else:
        print(line)
        failFile.write(line)   
f.close()
passFile.close() 
failFile.close()