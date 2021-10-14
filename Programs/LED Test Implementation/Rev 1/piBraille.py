#import libraries
import RPi.GPIO as GPIO

#set up GPIO. This programm will use the BCM numbering
GPIO.setmode(GPIO.BCM)

#set up library for alphabet
dict = {}
dict[str('A')] = [1,0,0,0,0,0]
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
dict[str('Y')] = [1,1,1,1,1,1]
dict[str('Z')] = [1,0,1,0,1,1]

#set up the output pins
tl = 2
ml = 3
bl = 4
tr = 17
mr = 27
br = 22

GPIO.setup(tl, GPIO.OUT)
GPIO.setup(ml, GPIO.OUT)
GPIO.setup(bl, GPIO.OUT)
GPIO.setup(tr, GPIO.OUT)
GPIO.setup(mr, GPIO.OUT)
GPIO.setup(br, GPIO.OUT)


outputStr = []

while(1):
    ltr = raw_input("Enter word: ")
    inputSize = len(ltr)
    
    for i in range(inputSize):
        searchLtr = ltr[i]
        if ltr[i] in dict:
            if dict[searchLtr][0] == 1:
                #tl = 'x'
                GPIO.output(tl, GPIO.HIGH)
            else:
                #tl = 'o'
                GPIO.output(tl, GPIO.LOW)
            if dict[searchLtr][1] == 1:
                #ml = 'x'
                GPIO.output(ml, GPIO.HIGH)
            else:
                #ml = 'o'
                GPIO.output(ml, GPIO.LOW)
            if dict[searchLtr][2] == 1:
                #bl = 'x'
                GPIO.output(bl, GPIO.HIGH)
            else:
                #bl = 'o'
                GPIO.output(bl, GPIO.LOW)
            if dict[searchLtr][3] == 1:
                #tr = 'x'
                GPIO.output(tr, GPIO.HIGH)
            else:
                #tr = 'o'
                GPIO.output(tr, GPIO.LOW)
            if dict[searchLtr][4] == 1:
                #mr = 'x'
                GPIO.output(mr, GPIO.HIGH)
            else:
                #mr = 'o'
                GPIO.output(mr, GPIO.LOW)
            if dict[searchLtr][5] == 1:
                #br = 'x'
                GPIO.output(br, GPIO.HIGH)
            else:
                #br = 'o'
                GPIO.output(br, GPIO.LOW)
        
        #print(tl+"\t"+tr+"\n"+ml+"\t"+mr+"\n"+bl+"\t"+br)
        #outputStr.append(tl+"\t"+tr+"\n"+ml+"\t"+mr+"\n"+bl+"\t"+br)
        
        i=i+1

    #print("\n")
    



