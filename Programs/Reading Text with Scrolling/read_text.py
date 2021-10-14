#opening target file
textFile = open('textFile.txt', 'r')

#read all lines into stringFile array
stringFile = textFile.read().split('\n')

#determine number of lines in the file
numLines = len(stringFile)

#initialize array that will store each element in file
textFileArray = []

for i in range(numLines):
    for j in range (len(stringFile[i])):
        if (stringFile[i][j] == " " or stringFile[i][j] == "\x0c"):
            j=j+1
        else:
            textFileArray.append(stringFile[i][j])
            j=j+1
    i=i+1
    
