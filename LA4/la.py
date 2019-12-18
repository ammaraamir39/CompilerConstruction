import regex
lineNumber=0
keywords = {
    'DT':['int','Decimal', 'var', 'string','bool'],
    'AOP': ['=' , '+=' , '-=' , '/=' , '%=' , '*='],
    'Terminator':[';'],
    'For':['for'],
    'ForEach':['foreach'],
    'in': ['in'],
    'if':['if'],
    'else':['else'],
    'elif':['elif'],
    'break': ['break'], 
    'Continue':['continue'],
    'Return': ['goback'],
    'Class': ['class'],
    'Public': ['public'],
    'Private': ['private'],
    'Protected': ['protected'],
    #'Inc/Dec':['++','--'],
    'MathPM':[ '+', '-'],
    'MathMDM':[ '/', '*', '%'],
    'RelationalOperators': ['<' , '>' , '<=' , '>=' , '==' , '!='],
    'AND': ['and'],
    'OR' :['or'],
    'NOT': ['not'],
     'Void':['void'], 
    'Static':['static'], 
    'Main':['main'],
    'this':['this'],
    'Virtual':['virtual'],
    '[': '[',
    ']': ']',
    '{': '{',
    '}': '}',
    '(': '(',
    ')': ')',
    ',' : ',',
    ':' : ':',
    'Dot' : '.',
    'Comments':'!!',
    'While':['while']

    

    }

#retreiving code from text file character by character

#class for token
class Token:
    def __init__(self, ClassPart, ValuePart,LineNumber):
        self.CP=ClassPart
        self.VP=ValuePart
        self.LN=LineNumber



programArray=[]
with open("program.txt") as f:
  while True:
    c = f.read(1)
    programArray.append(c)
    if not c:
      print ("End of file")
      break
    #print(c)

arr=[]
TS=[]

def tokenGenerate(word,lineNumber):
    #f=open("tokens.txt","w+")
    if(word == " " or word == ''):
        return
    #if word in keywords:
    classs = "Nahi hai"
    flag = 0
    for key in keywords:
        for value in keywords[key]:
            if word == value:
                classs= key
                flag = 1
    if flag == 0:
        
        if regex.identifier(word):
            classs = 'Id'
            flag = 0
        elif regex.integerConst(word):
            classs = 'IntegerConstant'
            flag = 0     
        elif regex.stringConstant(word):
            classs = 'StringConstant'
            word = word[1:len(word)-1]

            flag = 0
        elif regex.DecimalConst(word):
            classs = 'DecimalConstant'
            flag = 0

        elif regex.Comments(word):
            classs = 'Comments'
            flag = 0
        else:
            #print("Invalid Lexeme")
            classs = "Invalid Lexeme"
    
   
    
    print("(" + "'"+classs+"'" +","+ "'" + word +"'" + "," +  str(lineNumber)  + ")" )
    token = "(" + "'"+classs+"'" +","+ "'" + word +"'" + "," +  str(lineNumber)  + ")"
   
    #Token A(classs,word,str(lineNumber))
    A=Token(classs,word,str(lineNumber))
    TS.append(A)
   
    fileWrite(token)    

def fileWrite(token):
    f = open("token.txt", "a+")
    
    f.write(token + "\n")
    f.close()





#checking operator
def checkoperatorandBrackets(character):
    operator_brackets =   [ '+', '-', '/', '*', '%','<' , '>' ,'=', '<=' , '>=' , '==' ,'!', '!=', 'and', 'or', 'not', '{', '}', '[' , ']' , '(' , ')', ',', ':', '.',';']
    
    if character in operator_brackets:
        #print('found' + character)
        return True

def wordbreaking(character):
    
    if character=='!!' or character == ' ' or character == '\n' or character == ',' or character == ''or character == '(' or  checkoperatorandBrackets(character):
        #if(character == '<' or character == '>' or charcter )
        return True

def nextCharacter(character,nextChar):
    if character == '+' or character == '-' or character == '=' or character == '>' or character == '<' or character == '!':
        if nextChar == '+' or nextChar == '-' or nextChar == '=':
            word = character+nextChar
            for val in ['++','--','==','<=' , '>=' , '==' , '!=','+=']:
                if val == word:
                    return True
               

def matching(ProgArray):
    lineNumber = 1
    word = ""
    i=0

    while(i < len(ProgArray)):
        character = ProgArray[i]
        
        if (character == '!' and ProgArray[i+1] == '!'):
            
            word = character+ProgArray[i+1]
            character = ProgArray[i+2]
            i += 2
            #print(ProgArray[i])
            while(character != "!" and i < len(ProgArray)):
                    #print(len(ProgArray))
                    #print(i)
                if character != '\n':
                    word += character
                    #print(word)
                    i += 1
                    character = ProgArray[i]
                else:
                    i+=1
                    character=ProgArray[i]
            if(character == '!'):
                word += character+ProgArray[i+1]
                character=''
                i+=1


            #character=ProgArray[i]+ProgArray[i+1]
       
        if (character=='"' and i<len(ProgArray)):
            if word!= '':
                tokenGenerate(word,lineNumber)
            word=character
            character= ProgArray[i+1]
            #nxtChar = character+ ProgArray[i+1]+ ProgArray[i+2]

            i+=1
           # print(ProgArray[i-1]+character)
            while(character != '"' ):
                twochar = character + ProgArray[i+1]
                if(twochar == '\\\\'):
                    character = twochar
                    i +=1
                elif(twochar == '\\"'):

                    #word += (ProgArray[i-1]+character)
                    character = twochar
                    #print(character+ProgArray[i+1])
                    i = i+1
                     

                if character == '\n':
                    character = ""
                    break
                word+=character
                i += 1

                character=ProgArray[i]
            word+=character    
            tokenGenerate(word,lineNumber)
            i += 1
            character=ProgArray[i]
            word= ''
    
        if character == '.':
            #flag = 0
            if regex.integerConst(word):
                word += character
                #i +=1
                character = ProgArray[i+1]
            elif (regex.integerConst(word) == False) and (word != ''):
                tokenGenerate(word,lineNumber) 
                word = character
                character = programArray[i+1]
            else:
                word = character
                character = programArray[i+1]

            while regex.integerConst(character) == True:
                    word += character
                    i +=1
                    character = ProgArray[i+1]
                    #flag = 1
            

            #if flag == 1:
            #    word +=character
        
            tokenGenerate(word,lineNumber)
            word= ''
            

        elif wordbreaking(character):
            tokenGenerate(word,lineNumber)
            word = ''
            if  checkoperatorandBrackets(character):
                nextChar = ProgArray[i+1]
                if(nextCharacter(character,nextChar)):
                    word = character + nextChar
                    i +=1
                else:       
                    word = character
                tokenGenerate(word,lineNumber)
                word = ''
            if character == '\n':
                lineNumber +=1
            
        else:
            word += character
        
        i = i+1
    dallar = Token("$", "$",str(lineNumber))
    TS.append(dallar)
    

matching(programArray)

#TS.append(dallar)


    
#stringConstant('"ali_123"')
#c = '\n'

#charConstant(c)

