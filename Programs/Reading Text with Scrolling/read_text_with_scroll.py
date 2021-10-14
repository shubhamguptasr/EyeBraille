import pygame
import time


#opening target file
textFile = open('textFile.txt', 'r')

#read all lines into stringFile array
stringFile = textFile.read().split('\n')

#determine number of lines in the file
numLines = len(stringFile)

#initialize array that will store each element in file
textFileArray = []
scrollDir = 0
textPos = -1

for i in range(numLines):
    for j in range (len(stringFile[i])):
        if (stringFile[i][j] == " " or stringFile[i][j] == "\x0c"):
            j=j+1
        else:
            textFileArray.append(stringFile[i][j])
            j=j+1
i=i+1
    

screen = pygame.display.set_mode((320,240))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if((textPos==0 or textPos==-1) and e.button == 5):
                print("You are at the beginning of the document!")
            elif e.button == 4:
                print(textFileArray[textPos+1])
                textPos = textPos + 1
            elif e.button == 5:
                print(textFileArray[textPos-1])
                textPos = textPos - 1

   


    time.sleep(0.05)
    pygame.display.update()


    

