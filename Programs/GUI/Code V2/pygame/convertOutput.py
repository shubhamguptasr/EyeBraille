#import libraries
#import RPi.GPIO as GPIO
import pygame
import time

#set up GPIO. This programm will use the BCM numbering
#GPIO.setmode(GPIO.BCM)

#def convert():
    #set up library for alphabet
dict = {}
dict[str('A')] = [1,0,0,0,0,0]#start of upper case letters
dict[str('B')] = [1,1,0,0,0,0]
dict[str('C')] = [1,0,0,1,0,0]
dict[str('D')] = [1,0,0,1,1,0]
dict[str('E')] = [1,0,0,0,1,0]
dict[str('F')] = [1,1,0,1,0,0]
dict[str('G')] = [1,1,0,1,1,0]
dict[str('H')] = [1,1,0,0,1,0]
dict[str('I')] = [0,1,0,1,0,0]
dict[str('J')] = [0,1,0,1,1,0]
dict[str('K')] = [1,0,1,0,0,0]
dict[str('L')] = [1,1,1,0,0,0]
dict[str('M')] = [1,0,1,1,0,0]
dict[str('N')] = [1,0,1,1,1,0]
dict[str('O')] = [1,0,1,0,1,0]
dict[str('P')] = [1,1,1,1,0,0]
dict[str('Q')] = [1,1,1,1,1,0]
dict[str('R')] = [1,1,1,0,1,0]
dict[str('S')] = [0,1,1,1,0,0]
dict[str('T')] = [0,1,1,1,1,0]
dict[str('U')] = [1,0,1,0,0,1]
dict[str('V')] = [1,1,1,0,0,1]
dict[str('W')] = [0,1,0,1,1,1]
dict[str('X')] = [1,0,1,1,0,1]
dict[str('Y')] = [1,0,1,1,1,1]
dict[str('Z')] = [1,0,1,0,1,1]
dict[str('a')] = [1,0,0,0,0,0]#start of lower case letters
dict[str('b')] = [1,1,0,0,0,0]
dict[str('c')] = [1,0,0,1,0,0]
dict[str('d')] = [1,0,0,1,1,0]
dict[str('e')] = [1,0,0,0,1,0]
dict[str('f')] = [1,1,0,1,0,0]
dict[str('g')] = [1,1,0,1,1,0]
dict[str('h')] = [1,1,0,0,1,0]
dict[str('i')] = [0,1,0,1,0,0]
dict[str('j')] = [0,1,0,1,1,0]
dict[str('k')] = [1,0,1,0,0,0]
dict[str('l')] = [1,1,1,0,0,0]
dict[str('m')] = [1,0,1,1,0,0]
dict[str('n')] = [1,0,1,1,1,0]
dict[str('o')] = [1,0,1,0,1,0]
dict[str('p')] = [1,1,1,1,0,0]
dict[str('q')] = [1,1,1,1,1,0]
dict[str('r')] = [1,1,1,0,1,0]
dict[str('s')] = [0,1,1,1,0,0]
dict[str('t')] = [0,1,1,1,1,0]
dict[str('u')] = [1,0,1,0,0,1]
dict[str('v')] = [1,1,1,0,0,1]
dict[str('w')] = [0,1,0,1,1,1]
dict[str('x')] = [1,0,1,1,0,1]
dict[str('y')] = [1,0,1,1,1,1]
dict[str('z')] = [1,0,1,0,1,1]
dict[str('numInd')] = [0,0,1,1,1,1] #this is used as the indicator when going from letter to numbers
dict[str('1')] = [1,0,0,0,0,0]#start of numbers
dict[str('2')] = [1,1,0,0,0,0]
dict[str('3')] = [1,0,0,1,0,0]
dict[str('4')] = [1,0,0,1,1,0]
dict[str('5')] = [1,0,0,0,1,0]
dict[str('6')] = [1,1,0,1,0,0]
dict[str('7')] = [1,1,0,1,1,0]
dict[str('8')] = [1,1,0,0,1,0]
dict[str('9')] = [0,1,0,1,0,0]
dict[str('0')] = [0,1,0,1,1,0]
dict[str('puncInd')] = [0,0,0,1,1,1] #this is used as the indicator for punctuations
dict[str(',')] = [0,0,1,0,0,0]#start of punctuation
dict[str(':')] = [0,1,0,0,1,0]
dict[str('!')] = [0,1,1,0,1,0]
dict[str('.')] = [0,1,0,0,1,1]
dict[str('?')] = [0,1,1,0,0,1]
dict[str(';')] = [0,1,1,0,0,0]


#set up the output pins
tl = 2
ml = 3
bl = 4
tr = 17
mr = 27
br = 22

#GPIO.setup(tl, GPIO.OUT)
#GPIO.setup(ml, GPIO.OUT)
#GPIO.setup(bl, GPIO.OUT)
#GPIO.setup(tr, GPIO.OUT)
#GPIO.setup(mr, GPIO.OUT)
#GPIO.setup(br, GPIO.OUT)



#opening target file
textFile = open('Text_File.txt', 'r')

#read all lines into stringFile array
stringFile = textFile.read().split('\n')

#determine number of lines in the file
numLines = len(stringFile)

#initialize array that will store each element in file
textFileArray = []
scrollDir = 0
textPos = -1
letterToPrint = ""

for i in range(numLines):
    for j in range (len(stringFile[i])):
        if (stringFile[i][j] == " " or stringFile[i][j] == "\x0c"):
            j=j+1
        else:
            textFileArray.append(stringFile[i][j])
            j=j+1
i=i+1
    
#initialize screen size for pygame
screen = pygame.display.set_mode((320,240))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            if((textPos==0 or textPos==-1) and e.button == 5):
                print("You are at the beginning of the document!")
                #PLAY AUDIO HERE
            elif e.button == 4: #positive direction sequence
                if((ord(textFileArray[textPos])>=65 and ord(textFileArray[textPos])<=122) and (ord(textFileArray[textPos+1])>=48 and ord(textFileArray[textPos+1])<=58)):
                    print("numInd")
                    print('o'+"\t"+'x'+"\n"+'o'+"\t"+'x'+"\n"+'x'+"\t"+'x')
                    #GPIO.output(tl, GPIO.LOW)
                    #GPIO.output(ml, GPIO.LOW)
                    #GPIO.output(bl, GPIO.HIGH)
                    #GPIO.output(tr, GPIO.HIGH)
                    #GPIO.output(mr, GPIO.HIGH)
                    #GPIO.output(br, GPIO.HIGH)
                    
                elif((ord(textFileArray[textPos+1])==44) or (ord(textFileArray[textPos+1])==58) or (ord(textFileArray[textPos+1])==33) or (ord(textFileArray[textPos+1])==46) or (ord(textFileArray[textPos+1])==63) or (ord(textFileArray[textPos+1])==59)):
                    print("puncInd")
                    print('o'+"\t"+'x'+"\n"+'o'+"\t"+'x'+"\n"+'o'+"\t"+'x')
                    #GPIO.output(tl, GPIO.LOW)
                    #GPIO.output(ml, GPIO.LOW)
                    #GPIO.output(bl, GPIO.LOW)
                    #GPIO.output(tr, GPIO.HIGH)
                    #GPIO.output(mr, GPIO.HIGH)
                    #GPIO.output(br, GPIO.HIGH)
                    
                letterToPrint = textFileArray[textPos+1]
                textPos = textPos + 1
            elif e.button == 5: #negative direction sequence
                if((ord(textFileArray[textPos])>=65 and ord(textFileArray[textPos])<=122) and (ord(textFileArray[textPos-1])>=48 and ord(textFileArray[textPos-1])<=58)):
                    print("numInd")
                    print('o'+"\t"+'x'+"\n"+'o'+"\t"+'x'+"\n"+'x'+"\t"+'x')
                    #GPIO.output(tl, GPIO.LOW)
                    #GPIO.output(ml, GPIO.LOW)
                    #GPIO.output(bl, GPIO.HIGH)
                    #GPIO.output(tr, GPIO.HIGH)
                    #GPIO.output(mr, GPIO.HIGH)
                    #GPIO.output(br, GPIO.HIGH)

                elif((ord(textFileArray[textPos-1])==44) or (ord(textFileArray[textPos-1])==58) or (ord(textFileArray[textPos-1])==33) or (ord(textFileArray[textPos-1])==46) or (ord(textFileArray[textPos-1])==63) or (ord(textFileArray[textPos-1])==59)):
                    print("puncInd")
                    print('o'+"\t"+'x'+"\n"+'o'+"\t"+'x'+"\n"+'o'+"\t"+'x')
                    #GPIO.output(tl, GPIO.LOW)
                    #GPIO.output(ml, GPIO.LOW)
                    #GPIO.output(bl, GPIO.LOW)
                    #GPIO.output(tr, GPIO.HIGH)
                    #GPIO.output(mr, GPIO.HIGH)
                    #GPIO.output(br, GPIO.HIGH)
                    
                letterToPrint = textFileArray[textPos-1]
                textPos = textPos - 1
            
            if letterToPrint in dict:
                if dict[letterToPrint][0] == 1:
                    tl = 'x'
                    #GPIO.output(tl, GPIO.HIGH)
                else:
                    tl = 'o'
                    #GPIO.output(tl, GPIO.LOW)
                if dict[letterToPrint][1] == 1:
                    ml = 'x'
                    #GPIO.output(ml, GPIO.HIGH)
                else:
                    ml = 'o'
                    #GPIO.output(ml, GPIO.LOW)
                if dict[letterToPrint][2] == 1:
                    bl = 'x'
                    #GPIO.output(bl, GPIO.HIGH)
                else:
                    bl = 'o'
                    #GPIO.output(bl, GPIO.LOW)
                if dict[letterToPrint][3] == 1:
                    tr = 'x'
                    #GPIO.output(tr, GPIO.HIGH)
                else:
                    tr = 'o'
                    #GPIO.output(tr, GPIO.LOW)
                if dict[letterToPrint][4] == 1:
                    mr = 'x'
                    #GPIO.output(mr, GPIO.HIGH)
                else:
                    mr = 'o'
                    #GPIO.output(mr, GPIO.LOW)
                if dict[letterToPrint][5] == 1:
                    br = 'x'
                    #GPIO.output(br, GPIO.HIGH)
                else:
                    br = 'o'
                    #GPIO.output(br, GPIO.LOW)
            print(tl+"\t"+tr+"\n"+ml+"\t"+mr+"\n"+bl+"\t"+br)



    time.sleep(0.05)
    pygame.display.update()
