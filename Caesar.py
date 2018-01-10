class Caesar(object):
    __letterToNumber = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
    __numberToLetter = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

    def encrypt(self, text, key):
        output = ""
        
        key = key.upper()
        key = self.__letterToNumber[key]
        
        for i in text:
            if i in self.__letterToNumber:
                letter = self.__letterToNumber[i]
                letter = int((letter + key) % 26)            
                letter = self.__numberToLetter[letter]
                output += str(letter)
            else:
                output += i
        
        return output

    def decrypt(self, text, key):
        output = ""
        
        key = key.upper()
        key = self.__letterToNumber[key]
        
        for i in text:
            if i in self.__letterToNumber:
                letter = self.__letterToNumber[i]
                letter = int(abs((letter - key) % 26))            
                letter = self.__numberToLetter[letter]
                output += str(letter)
            else:
                output += i
        
        return output

    def bruteForce(self, input):
        maxWordLength = 0
        maxWord = ""
        wordList = list(input.split())
        
        for i in wordList:
            if len(i) > maxWordLength:
                maxWordLength = len(i)
                maxWord = i
        
        tester = Caesar(maxWord)
        
        print("Brute Force Tests:")
        for i in range(0,26,1):
            key = self.__numberToLetter[i]            
            print(key, "\t" ,tester.decrypt(key))
            
    def findKey(self, input):
        dict2 = ("IN","IM","AM","AN","UM","ER","ES","ZU")
        dict3 = ("DER","DIE","DAS","DEN","DEM","DES","VON","VOM","UND","IST")
        wordListComplete = list(input.split())
        wordList2 = []
        wordList3 = []
        max2Letter = ""
        max2Val = 0
        max3Letter = ""
        max3Val = 0
        
        for i in wordListComplete:
            if len(i) == 2:
                wordList2.append(i)
            elif len(i) == 3:
                wordList3.append(i)
            
        tester = Caesar("")
        
        for i in range(0,26,1):
            tempCount = 0
            for j in wordList2:
                tester.setInput(j)                
                if tester.decrypt(self.__numberToLetter[i]) in dict2:
                    tempCount += 1
            if tempCount >= max2Val:
                max2Val = tempCount
                max2Letter = self.__numberToLetter[i]
        
        for i in range(0,26,1):
            tempCount = 0
            for j in wordList3:
                tester.setInput(j)                
                if tester.decrypt(self.__numberToLetter[i]) in dict3:
                    tempCount += 1
            if tempCount >= max3Val:
                max3Val = tempCount
                max3Letter = self.__numberToLetter[i]        
        
        if (max2Letter == max3Letter):
            print("Result:\t", max2Letter)
        else:
            print("Result:\t", max2Letter, " or ", max3Letter)
    
