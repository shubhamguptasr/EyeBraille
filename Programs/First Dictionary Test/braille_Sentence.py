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

tl = 'o'
ml = 'o'
bl = 'o'
tr = 'o'
mr = 'o'
br = 'o'

outputStr = []

while(1):
    ltr = raw_input("Enter word: ")
    inputSize = len(ltr)
    
    for i in range(inputSize):
        searchLtr = ltr[i]
        if ltr[i] in dict:
            if dict[searchLtr][0] == 1:
                tl = 'x'
            else:
                tl = 'o'
            if dict[searchLtr][1] == 1:
                ml = 'x'
            else:
                ml = 'o'
            if dict[searchLtr][2] == 1:
                bl = 'x'
            else:
                bl = 'o'
            if dict[searchLtr][3] == 1:
                tr = 'x'
            else:
                tr = 'o'
            if dict[searchLtr][4] == 1:
                mr = 'x'
            else:
                mr = 'o'
            if dict[searchLtr][5] == 1:
                br = 'x'
            else:
                br = 'o'
        
        #print(tl+"\t"+tr+"\n"+ml+"\t"+mr+"\n"+bl+"\t"+br)
        outputStr.append(tl+"\t"+tr+"\n"+ml+"\t"+mr+"\n"+bl+"\t"+br)
        
        i=i+1

    print("\n")
    for i in range(len(outputStr)):
        print(outputStr[i]+'\t')
        i=i+1



