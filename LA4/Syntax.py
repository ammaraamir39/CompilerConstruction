import cpv
import la
import allClassAndFunctions


TokenSet=[]
TokenSet=la.TS

SymbolTableArray=[] #array of Symbol Table 
ClassDefArray=[] #array of Class Table
ClassTableArray=[] #array of Class 
FunctionTableArray=[] #array of function table
TemporaryTableArray=[] #array of tempororary 





class Index:
    def __init__(self):
        self.value=0




def SyntaxAnalyzer(index,TokenSet):
       if start(index,TokenSet):
           print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


def start(index,TokenSet):
    if(TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == cpv.DT or TokenSet[index.value].CP == cpv.Void or TokenSet[index.value].CP == cpv.If or TokenSet[index.value].CP == cpv.Return or TokenSet[index.value].CP == cpv.Break or TokenSet[index.value].CP == cpv.Static or TokenSet[index.value].CP == cpv.This or   TokenSet[index.value].CP == cpv.Class or TokenSet[index.value].CP == cpv.For or TokenSet[index.value].CP=="While" ):
        
        if(SST2(index,TokenSet)):
            if(TokenSet[index.value].CP==cpv.Terminator):
                index.value+=1
                #if(TokenSet[index.value]==cpv.Terminator):
                 #   index.value+=1
                if(start(index,TokenSet)):
                        return True
    elif(TokenSet[index.value].CP=="$"):
        
        return True
    else:
        print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
        return False

def DT2(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.DT):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP =="Id"):
        index.value+=1
        return True    
    else:
        return False

def CONST(index,TokenSet):
    if(TokenSet[index.value].CP == "IntegerConstant"):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP == "StringConstant"):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP == "DecimalConstant"):
        index.value+=1
        return True    
    else:
        return False


def DATA(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant"):
        if(CONST(index,TokenSet)):
            return True
    else:
        return False

def Decl2(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.Void):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(TokenSet[index.value].CP=="("):
                index.value+=1
                if(args(index,TokenSet)):
                        if(TokenSet[index.value].CP==")"):
                            index.value+=1
                            if(funcBody(index,TokenSet)):
                                
                                    if(TokenSet[index.value].CP=="Terminator"):
                                        return True
    else:
        return False

def Decl3(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.Static or TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP=="Id"):
        if(Static(index,TokenSet)):
            if(DT2(index,TokenSet)):
                if(TokenSet[index.value].CP=="Id"):
                    index.value+=1
                    if(TokenSet[index.value].CP=="Terminator"):
                        return True
    else:
        return False


def List(index,TokenSet):
    if(TokenSet[index.value].CP=="("):
        index.value+=1
        if(args(index,TokenSet)):
            if(TokenSet[index.value].CP==")"):
                index.value+=1
                if(funcBody(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP==cpv.AOP):

        if(list1(index,TokenSet)):
            if(list2(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP=="Terminator"):
                    return True        

    
    return False

        
def list1(index,TokenSet):
    if(TokenSet[index.value].CP=="["):
        index.value+=1
        if(INDEXCHOOSE(index,TokenSet)):
            if(TokenSet[index.value].CP=="]"):
                index.value+=1
                if(list4(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(OE(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="," or TokenSet[index.value].CP==cpv.Terminator):
        return True
    return False

def INDEXCHOOSE(index,TokenSet):
    if(TokenSet[index.value].CP=="Id" or TokenSet[index.value].CP=="(" or TokenSet[index.value].CP=="IntegerConstant" or  TokenSet[index.value].CP=="NOT" or TokenSet[index.value].CP==cpv.This or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant"):
        if(OE(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="]"):
        return True

    return False

def list2(index,TokenSet):
    if(TokenSet[index.value].CP==","):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(list1(index,TokenSet)):
                if(list2(index,TokenSet)):
                    return True
                   
    elif(TokenSet[index.value].CP=="Terminator"):
        return True
    
    return False

def list3(index,TokenSet):
    if(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="="):
        if(list1(index,TokenSet)):
            if(list2(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP=="Terminator"):
        return True
    
    return False               

def list4(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(ARRAYBODY(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="," or TokenSet[index.value].CP==cpv.Terminator):
        return True
    return False


def ARRAYBODY(index,TokenSet):
    if(TokenSet[index.value].CP=="{"):
        index.value+=1
        if(OE(index,TokenSet)):
            if(ARRAYBODY2(index,TokenSet)):
                if(TokenSet[index.value].CP=="}"):
                    index.value+=1
                   # if(TokenSet[index.value].CP==cpv.Terminator):
                    #    index.value+=1
                    return True
    
    return False                

def  ARRAYBODY2(index,TokenSet):
    if(TokenSet[index.value].CP==","):
        index.value+=1
        if(OE(index,TokenSet)):
            if(ARRAYBODY2(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP=="}"):
        return True

    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP) 
    return False

def args(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP=="Id"):
        if(DT2(index,TokenSet)):
            if(ID2(index,TokenSet)):
                if(args2(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP==")"):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def ID2(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        return True
    elif( TokenSet[index.value].CP==")" or TokenSet[index.value].CP==","):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def args2(index,TokenSet):
    if(TokenSet[index.value].CP==","):
        index.value+=1
        if(args(index,TokenSet)):
            if(args2(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==")"):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    



def Static(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.Static):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP=="Id"):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def Assignment_st2(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.This):
        index.value+=1
        if(TokenSet[index.value].CP=="Dot"):
            index.value+=1
            if(TokenSet[index.value].CP=="Id"):
                index.value+=1
                if(func1(index,TokenSet)):
                    if(aur(index,TokenSet)):
                        if(TokenSet[index.value].CP==cpv.AOP):
                            index.value+=1
                            if(OE(index, TokenSet)):
                                return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    
def func1(index,TokenSet):
    if(TokenSet[index.value].CP=="("):
        
        if(params(index,TokenSet)):
            if(aur(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.AOP or TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="."):
        return True
    
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def aur(index,TokenSet):
    if(TokenSet[index.value].CP=="["):
        index.value+=1
        if(OE(index,TokenSet)):
            if(TokenSet[index.value].CP=="]"):
                index.value+=1
                if(aur2(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP=="Dot"):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(aur(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.AOP or TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP==cpv.Terminator or TokenSet[index.value].CP=="("):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def aur2(index,TokenSet):
    if(TokenSet[index.value].CP=="Dot"):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(aur(index,TokenSet)):
                return True
    
    
    elif(TokenSet[index.value].CP==cpv.AOP or TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP=="("):
        return True
    
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def aur3(index,TokenSet):
    if(TokenSet[index.value].CP=="["):
        index.value+=1
        if(OE(index,TokenSet)):
            if(TokenSet[index.value].CP == "]"):
                index.value+= 1
                if(TokenSet[index.value].CP=="Dot"):
                    index.value+=1
                    if(TokenSet[index.value].CP=="Id"):
                        index.value+=1
                        if(aur(index,TokenSet)):
                            return True
    elif(TokenSet[index.value].CP == "Dot"):
        index.value+=1
        if(TokenSet[index.value].CP == "Id"):
                        index.value+=1
                        if(aur(index, TokenSet)):
                            return True
    elif(TokenSet[index.value].CP=="("):
        return True 
    
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def Body(index,TokenSet):
        if(TokenSet[index.value].CP=="{"):
            index.value+=1
            if(MST(index,TokenSet)):
                if(TokenSet[index.value].CP=="}"):
                    index.value+=1
                    return True

def MST(index,TokenSet):
    if(TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == cpv.DT  or TokenSet[index.value].CP == cpv.If or TokenSet[index.value].CP == cpv.Return or TokenSet[index.value].CP == cpv.Break or TokenSet[index.value].CP == cpv.Static or TokenSet[index.value].CP == cpv.This or TokenSet[index.value].CP == cpv.For):
        if(SST(index,TokenSet)):
            if(TokenSet[index.value].CP==cpv.Terminator):
                index.value+=1
                if(MST(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP=="}"):
        return True

    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def funcBody(index,TokenSet):
    if(TokenSet[index.value].CP=="{"):
        index.value+=1
        if(MST2(index,TokenSet)):
            if(TokenSet[index.value].CP=="}"):
                index.value+=1
                return True

    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def MST2(index,TokenSet):
    if(TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == cpv.DT or TokenSet[index.value].CP == cpv.Void or TokenSet[index.value].CP == cpv.If or TokenSet[index.value].CP == cpv.Return or TokenSet[index.value].CP == cpv.Break or TokenSet[index.value].CP == cpv.Static or TokenSet[index.value].CP == cpv.This or   TokenSet[index.value].CP == cpv.Class or TokenSet[index.value].CP == cpv.For ):
        if(SST2(index,TokenSet)):
            if(TokenSet[index.value].CP==cpv.Terminator):
                index.value+=1
                if(MST2(index,TokenSet)):
                    return True
    elif(TokenSet[index.value].CP=="}"):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False    

def SST(index,TokenSet):
    if(TokenSet[index.value].CP=="Id" or TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP==cpv.Static or TokenSet[index.value].CP==cpv.This):
        if(DAfunc(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.For):
        if(for_St(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.foreach):
        if(foreach(index, TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.If):
        if(if_st(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Return):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP==cpv.Break):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP == cpv.Continue):
        index.value+= 1
        return True
    elif(TokenSet[index.value].CP==cpv.DT):
        if(Object(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="While"):
        if(While_St(index,TokenSet)):
              
            return True
    
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def SST2(index,TokenSet):
    if(TokenSet[index.value].CP=="Id" or TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP==cpv.Void or TokenSet[index.value].CP==cpv.Static or TokenSet[index.value].CP==cpv.This):
        if(DA(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.For):
        if(for_St(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.foreach):
        if(foreach(index, TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="While"):
        if(While_St(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.If):
        if(if_st(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Return):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP==cpv.Break):
        index.value+=1
        return True
    elif(TokenSet[index.value].CP == cpv.Continue):
        index.value+= 1
        return True
    elif(TokenSet[index.value].CP==cpv.DT):
        if(Object(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Class):
        if(Classs(index,TokenSet)):
            return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False        


def for_St(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.For):
        index.value+=1
        if(TokenSet[index.value].CP=="("):
            index.value+=1
            if(forCond(index,TokenSet)):
                if(TokenSet[index.value].CP==")"):
                    index.value+=1
                    if(funcBody(index,TokenSet)):

                        return True
    
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False        


def forCond(index,TokenSet):
    if(TokenSet[index.value].CP=="Id" or TokenSet[index.value].CP==","):
        if(forCond4(index,TokenSet)):
            if(forCond2(index,TokenSet)):
                return True
    
    return False

def forCond2(index,TokenSet):
    if(TokenSet[index.value].CP=="," ):
        index.value+=1
        if(forCond3(index,TokenSet)):
            if(TokenSet[index.value].CP==","):
                index.value+=1
                if(forCond4(index,TokenSet)):
                    return True
    return False    

def forCond3(index,TokenSet):
    if(TokenSet[index.value].CP=="Id" or TokenSet[index.value].CP=="(" or TokenSet[index.value].CP=="IntegerConstant" or  TokenSet[index.value].CP=="NOT" or TokenSet[index.value].CP==cpv.This or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant"):
        if(OE(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==","):
        return True
    return False

def forCond4(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(TokenSet[index.value].CP==cpv.AOP):
            index.value+=1
            if(OE(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==")"):
        return True         

    return False

def While_St(index,TokenSet):
    if(TokenSet[index.value].CP=="While"):
        index.value+=1
        if(TokenSet[index.value].CP=="("):
            index.value+=1
            if(OE(index,TokenSet)):
                if(TokenSet[index.value].CP==")"):
                    index.value+=1
                    if(funcBody(index,TokenSet)):
                        return True
    
    return False


def foreach(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.foreach):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(TokenSet[index.value].CP==cpv.In):
                index.value+=1
                if(TokenSet[index.value].CP=="Id"):
                    index.value+=1
                    if(Body(index,TokenSet)):
                        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False                

def if_st(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.If):
        index.value+=1
        if(TokenSet[index.value].CP=="("):
            index.value+=1
            if(OE(index,TokenSet)):
                if(TokenSet[index.value].CP==")"):
                    index.value+=1
                    if(Body(index,TokenSet)):
                        if(Else(index,TokenSet)):
                            return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def Else(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.Elif):
        if(Elif(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Else):
        index.value+=1
        if(Body(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def Elif(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.Elif):
        index.value+=1
        if(TokenSet[index.value].CP=="("):
            index.value+=1
            if(OE(index,TokenSet)):
                if(TokenSet[index.value].CP==")"):
                    index.value+=1
                    if(Body(index,TokenSet)):
                        if(Else(index,TokenSet)):
                            return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def DA(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(DA1(index,TokenSet)):
            #if(TokenSet[index.value].CP==cpv.Terminator):
             #   index.value+=1
                return True

    elif(TokenSet[index.value].CP==cpv.DT):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(List(index,TokenSet)):
              #  if(TokenSet[index.value].CP==cpv.Terminator):
                    return True
    elif(TokenSet[index.value].CP==cpv.Void):
    
        if(Decl2(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Static or TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP=="Id"):
        
        if(Decl3(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.This):
        
        if(Assignment_st2(index,TokenSet)):
            return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def DA1(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(List(index,TokenSet)):
            return True
    #yeh neeche wala dekhna hai <func1> k bad AOP add hoga ya nahi 
    elif(TokenSet[index.value].CP=="(" ):
        if(params(index,TokenSet)):
            if(DA2(index,TokenSet)):
                return True
        
    elif(TokenSet[index.value].CP=="["):
        index.value+=1
        
        if(OE(index,TokenSet)):
            if(TokenSet[index.value].CP=="]"):
                index.value+=1
                if(TokenSet[index.value].CP=="Dot"):
                    index.value+=1
                    if(TokenSet[index].CP=="Id"):
                        index.value+=1
                        if(aur(index,TokenSet)):
                            if(params(index,TokenSet)):
                                return True

    elif(TokenSet[index.value].CP=="Dot"):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            # if(aur(index,TokenSet)):
            #     if(params(index,TokenSet)):
            #         return True
            if(APOE(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(OE(index,TokenSet)):
            return True


    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def APOE(index,TokenSet):
    if(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP=="("):
        if(aur(index,TokenSet)):
            if(params(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(OE(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
        return True

    return False

def DA2(index,TokenSet):
    if(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP==cpv.AOP ):
        if(aur(index,TokenSet)):
            # if(TokenSet[index.value].CP==cpv.AOP):
            #     index.value+=1
            #     if(OE(index,TokenSet)):
            #         return True
            if(DA3(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
         return True
    else:
        print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
        return False

def DA3(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(OE(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
        return True

    return False





def DAfunc(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(DAfunc1(index,TokenSet)):
            #if(TokenSet[index.value].CP==cpv.Terminator):
             #   index.value+=1
                return True
    elif(TokenSet[index.value].CP == cpv.DT):
        index.value+= 1
        if(TokenSet[index.value].CP == "Id"):
            index.value += 1
            if(list3(index, TokenSet)):
                #if(TokenSet[index.value].CP == cpv.Terminator):
                    return True
    elif(TokenSet[index.value].CP==cpv.Static or TokenSet[index.value].CP==cpv.DT or TokenSet[index.value].CP=="Id"):

        if(Decl3(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP == cpv.This):
        
        if(Assignment_st2(index, TokenSet)):
            return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def DAfunc1(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(list3(index,TokenSet)):
            return True
    #yeh neeche wala dekhna hai <func1> k bad AOP add hoga ya nahi 
    elif(TokenSet[index.value].CP=="(" ):
        if(params(index,TokenSet)):
            if(DAfunc2(index,TokenSet)):
                   return True
        
    elif(TokenSet[index.value].CP=="["):
        index.value+=1
        
        if(OE(index,TokenSet)):
            if(TokenSet[index.value].CP=="]"):
                index.value+=1
                if(TokenSet[index.value].CP=="Dot"):
                    index.value+=1
                    if(TokenSet[index].CP=="Id"):
                        index.value+=1
                        if(aur(index,TokenSet)):
                            if(params(index,TokenSet)):
                                return True

    elif(TokenSet[index.value].CP=="Dot"):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            # if(aur(index,TokenSet)):
            #     if(params(index,TokenSet)):
            #         return True
            if(APOE(index, TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.AOP):
        index.value+=1
        if(OE(index,TokenSet)):
            return True


    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def DAfunc2(index,TokenSet):
    if(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP==cpv.AOP):
        if(aur(index,TokenSet)):
            # if(TokenSet[index.value].CP==cpv.AOP):
            #     index.value+=1
            #     if(OE(index,TokenSet)):
            #         return True
            if(DAfunc3(index,TokenSet)):
                return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
        return True
    else:
        print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
        return False

def DAfunc3(index,TokenSet):
    if(TokenSet[index.value].CP == cpv.AOP):
        index.value += 1
        if(OE(index, TokenSet)):
            return True
    elif(TokenSet[index.value].CP==cpv.Terminator):
        return True

    return False



# def params(index,TokenSet):
#     if(TokenSet[index.value].CP=="("):
#         index.value+=1
#         if(OE(index,TokenSet)):
#             if(params2(index,TokenSet)):
#                 if(TokenSet[index.value].CP==")"):
#                     index.value+=1
#                     return True
#     print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
#     return False

# def params2(index,TokenSet):
#     if(TokenSet[index.value].CP==","):
#         index.value+=1
#         if(OE(index,TokenSet)):
#             if(params2(index,TokenSet)):
#                 return True
#     elif(TokenSet[index.value].CP==")"):
#         return True
#     print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
#     return False

def params(index,TokenSet):
    if(TokenSet[index.value].CP=="("):
        index.value+=1
        if(params2(index,TokenSet)):
            if(TokenSet[index.value].CP==")"):
                index.value+=1
                return True
    elif(TokenSet[index.value].CP=="[" or TokenSet[index.value].CP==cpv.Terminator or TokenSet[index.value].CP=="Dot" or TokenSet[index.value].CP==cpv.AOP):
        return True
    return False

def params2(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or TokenSet[index.value].CP== 'OR' or TokenSet[index.value].CP== 'AND' or TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if(OE(index,TokenSet)):
            if(params3(index,TokenSet)):
                return True 
    elif(TokenSet[index.value].CP==")"):
        return True
    
    return False

def params3(index,TokenSet):
        if(TokenSet[index.value].CP==","):
            index.value+=1
            if(OE(index,TokenSet)):
                if(params3(index,TokenSet)):
                    return True
        elif(TokenSet[index.value].CP==")"):
            return True
        return False

        

def Object(index,TokenSet):
    if(TokenSet[index.value].CP==cpv.DT):
        index.value+=1
        if(TokenSet[index.value].CP=="Id"):
            index.value+=1
            if(TokenSet[index.value].CP==cpv.AOP):
                index.value+=1
                if(TokenSet[index.value].CP=="{"):
                    index.value+=1
                    if(objectbody(index,TokenSet)):
                            if(TokenSet[index.value].CP=="}"):
                                index.value+=1
                                if(TokenSet[index.value].CP==cpv.Terminator):
                                    index.value+=1
                                    return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def objectbody(index,TokenSet):
    if(TokenSet[index.value].CP=="Id"):
        index.value+=1
        if(TokenSet[index.value].CP==cpv.AOP):
            index.value+=1
            if(params2(index,TokenSet)):
                if(objectbody2(index,TokenSet)):
                    return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def objectbody2(index,TokenSet):
    if(TokenSet[index.value].CP==","):
        index.value+=1
        if(objectbody(index,TokenSet)):
            return True
    elif(TokenSet[index.value].CP=="}"):
        return True
    print("Invalid Syntax @" + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
           





def Classs(index,TokenSet):
    if TokenSet[index.value].CP == "Class" :
        index.value+=1
        if TokenSet[index.value].CP == "Id" :
            index.value+=1
            if BaseClassName(index,TokenSet):
                if TokenSet[index.value].CP == "{" :
                    index.value+=1
                    if ClassBody(index,TokenSet):
                        if TokenSet[index.value].CP == "}" :
                            index.value+=1
                            return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    








def BaseClassName(index,TokenSet):
    if TokenSet[index.value].CP == "(" :
        index.value+= 1
        if TokenSet[index.value].CP == "Id" :
            index.value+=1
            if BaseClassName2(index,TokenSet):
                if TokenSet[index.value].CP == ")" :
                    index.value+=1
                    return True
    elif TokenSet[index.value].CP == "{" :
        return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


        

def BaseClassName2(index,TokenSet):
    if TokenSet[index.value].CP == "," :
        index.value+=1
        if TokenSet[index.value].CP == "Id" :
            index.value+=1
            if BaseClassName2(index,TokenSet):
                return True

    elif TokenSet[index.value].CP == ")" :
        return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def ClassBody(index,TokenSet):
    if TokenSet[index.value].CP == "Public" or TokenSet[index.value].CP == "Private" or TokenSet[index.value].CP == "Protected":
        if AM(index,TokenSet):
            if TokenSet[index.value].CP == ":":
                index.value+=1
                if ClassBody2(index,TokenSet):
                    if ClassBody(index,TokenSet):
                        return True
    elif(TokenSet[index.value].CP=="}"):
        return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


                    

def ClassBody2(index,TokenSet):
    if TokenSet[index.value].CP == "Static":
        if MA(index,TokenSet):
            return True
    elif TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == "DT":
        if MA4(index,TokenSet):
            return True
    elif TokenSet[index.value].CP == "Virtual":
        index.value+=1
        if RT(index,TokenSet):
                if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if TokenSet[index.value].CP == "(":
                        index.value+=1
                        if args(index,TokenSet):
                            if TokenSet[index.value].CP == ")":
                                index.value+=1
                                if TokenSet[index.value].CP == "AOP": #siyapa
                                    index.value+=1
                                    if TokenSet[index.value].CP == "IntegerConstant": #siyapa
                                        index.value+=1
                                        if(TokenSet[index.value].CP==cpv.Terminator):
                                            index.value+=1
                                            if ClassBody2(index,TokenSet):
                                                if constructor(index,TokenSet):
                                                    return True
    
    elif TokenSet[index.value].CP == "Void":
        index.value+=1
        if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if TokenSet[index.value].CP == "(":
                        index.value+=1
                        if args(index,TokenSet):
                            if TokenSet[index.value].CP == ")":
                                index.value+=1 
                                if funcBody(index,TokenSet):
                                    if ClassBody2(index,TokenSet):
                                        return True

    elif (TokenSet[index.value].CP == "}" or TokenSet[index.value].CP == "Public" or TokenSet[index.value].CP == "Private" or TokenSet[index.value].CP == "Protected" or TokenSet[index.value].CP=="Id"):
        return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def MA(index,TokenSet):
    if TokenSet[index.value].CP == "Static":
        index.value+=1
        if MA2(index,TokenSet):
            return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def MA2(index,TokenSet):
    if TokenSet[index.value].CP == "DT" or TokenSet[index.value].CP == "Id":
        if DT2(index,TokenSet):
            if TokenSet[index.value].CP == "Id":
                index.value+=1
                if MA3(index,TokenSet):
                    return True
                
    elif TokenSet[index.value].CP == "Void":
        index.value+=1
        if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if TokenSet[index.value].CP == "(":
                        index.value+=1
                        if args(index,TokenSet):
                            if TokenSet[index.value].CP == ")":
                                index.value+=1 
                                if funcBody(index,TokenSet):
                                    if ClassBody2(index,TokenSet):
                                        return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def MA3(index,TokenSet):
    if TokenSet[index.value].CP == "AOP":
        index.value+=1
        if OE(index,TokenSet):
            if TokenSet[index.value].CP == "Terminator":
                index.value+=1
                if ClassBody2(index,TokenSet):
                    return True

    elif  TokenSet[index.value].CP == "(":
        index.value+=1
        if args(index,TokenSet):
            if TokenSet[index.value].CP == ")":
                index.value+=1 
                if funcBody(index,TokenSet):
                    if ClassBody2(index,TokenSet):
                        return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def MA4(index,TokenSet):
    if TokenSet[index.value].CP == "DT" or TokenSet[index.value].CP == "Id":
            if(DT2(index,TokenSet)):
                if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if MA5(index,TokenSet):
                        return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def MA5(index,TokenSet):
    if TokenSet[index.value].CP == "[" or  TokenSet[index.value].CP == "AOP" or TokenSet[index.value].CP == "Terminator":
        if attributes2(index,TokenSet):
            if attributes3(index,TokenSet):
                if TokenSet[index.value].CP == "Terminator":
                    index.value+=1
                    if ClassBody2(index,TokenSet):
                        return True
    
    elif TokenSet[index.value].CP == "(":
        index.value+=1
        if args(index,TokenSet):
            if TokenSet[index.value].CP == ")":
                index.value += 1 
                if funcBody(index,TokenSet):
                    if ClassBody2(index,TokenSet):
                        return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def AM(index,TokenSet):
    if TokenSet[index.value].CP == "Public":
        index.value+= 1
        return True
    elif TokenSet[index.value].CP == "Private":
        index.value+= 1
        return True
    elif TokenSet[index.value].CP == "Protected":
        index.value+=1
        return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

'''
def attributes(index,TokenSet):
    if TokenSet[index.value].CP == "Static":
        index.value+=1
        if DT2(index,TokenSet):
            if TokenSet[index.value].CP == "Id":
                index.value+=1
                if TokenSet[index.value].CP == "AOP":
                    index.value+=1
                    if OE(index,TokenSet):
                        if TokenSet[index.value].CP == "Terminator":
                            index.value+=1
                            if ClassBody2(index,TokenSet):
                                return True
    elif TokenSet[index.value].CP == "DT" or TokenSet[index.value].CP == "Id" :
        if DT2(index,TokenSet):
            if TokenSet[index.value].CP == "Id":
                index.value+=1
                if attributes2(index,TokenSet):
                    if attributes3(index,TokenSet):
                        if TokenSet[index.value].CP == "Terminator":
                            index.value+=1
                            if ClassBody2(index,TokenSet):
                                return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
'''    


def attributes2(index,TokenSet):
    if TokenSet[index.value].CP == "[":
        index.value+=1
        if OE(index,TokenSet):
            if TokenSet[index.value].CP == "]":
                index.value+=1
                return True
    elif TokenSet[index.value].CP == "Terminator" or TokenSet[index.value].CP == 'AOP':
        return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def attributes3(index,TokenSet):
    if TokenSet[index.value].CP == "AOP":
        index.value+=1
        if OE(index,TokenSet):
            return True
    elif TokenSet[index.value].CP == "Terminator":
        return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    


'''
def methods(index,TokenSet):
    if TokenSet[index.value].CP == "Static" or TokenSet[index.value].CP == "DT" or TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == "Void":
        if static(index,TokenSet):
            if RT(index,TokenSet):
                if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if TokenSet[index.value].CP == "(":
                        index.value+=1
                        if args(index,TokenSet):
                            if TokenSet[index.value].CP == ")":
                                index.value+=1 
                                if funcBody(index,TokenSet):
                                    if ClassBody2(index,TokenSet):
                                        return True
    elif TokenSet[index.value].CP == "Virtual":
        index.value+=1
        if RT(index,TokenSet):
                if TokenSet[index.value].CP == "Id":
                    index.value+=1
                    if TokenSet[index.value].CP == "(":
                        index.value+=1
                        if args(index,TokenSet):
                            if TokenSet[index.value].CP == ")":
                                index.value+=1
                                if TokenSet[index.value].CP == "AOP": #siyapa
                                    index.value+=1
                                    if TokenSet[index.value].CP == "IntegerConstant": #siyapa
                                        index.value+=1
                                        if constructor(index,TokenSet):
                                            return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    
'''



def RT(index,TokenSet):
    if TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == "DT":
        if DT2(index,TokenSet):
            return True
    elif TokenSet[index.value].CP == "Void":
        index.value+=1
        return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
        

def constructor(index,TokenSet):
    if TokenSet[index.value].CP == "Id":
        if TokenSet[index.value].CP == "(":
            index.value+=1
            if args(index,TokenSet):
                if TokenSet[index.value].CP == ")":
                    index.value+=1 
                    if TokenSet[index.value].CP == "{":
                        index.value+=1
                        if Constructorbody(index,TokenSet):
                            if TokenSet[index.value].CP == "}":
                                index.value+=1
                                return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    



def Constructorbody(index,TokenSet):
    if TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP == "DT" or TokenSet[index.value].CP == "Void" or TokenSet[index.value].CP == "Static" or TokenSet[index.value].CP == "this":
        if DAfunc(index,TokenSet):
            if TokenSet[index.value].CP == "terminator":
                index.value+=1
                if Constructorbody(index,TokenSet):
                    return True
    elif TokenSet[index.value].CP == "}":
        return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def OE(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or TokenSet[index.value].CP== 'OR' or TokenSet[index.value].CP== 'AND' or TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if AE(index,TokenSet):
            if OEC(index,TokenSet):
                return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def OEC(index,TokenSet):
    if(TokenSet[index.value].CP == 'OR'):
        index.value+=1
        if AE(index,TokenSet):
            if OEC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP == "]" or TokenSet[index.value].CP == "," or TokenSet[index.value].CP == "Terminator" or TokenSet[index.value].CP == ")"):
        return True
        
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def AE(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or TokenSet[index.value].CP== 'OR' or TokenSet[index.value].CP== 'AND' or TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if EE(index,TokenSet):
            if AEC(index,TokenSet):
                return True
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def AEC(index,TokenSet):
    if(TokenSet[index.value].CP == 'AND'):
        index.value+=1
        if EE(index,TokenSet):
            if AEC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="]" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")"):
        return True
        
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def EE(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or TokenSet[index.value].CP== 'OR' or TokenSet[index.value].CP== 'AND' or TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if RE(index,TokenSet):
            if EEC(index,TokenSet):
                return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def EEC(index,TokenSet):
    if(TokenSet[index.value].CP == 'EQUALITY'):
        index.value+=1
        if RE(index,TokenSet):
            if EEC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="]" or TokenSet[index.value].CP=="AND" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")"):
        return True
        
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    False


def RE(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or TokenSet[index.value].CP== 'OR' or TokenSet[index.value].CP== 'AND' or TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if E(index,TokenSet):
            if REC(index,TokenSet):
                return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def REC(index,TokenSet):
    if(TokenSet[index.value].CP == 'RelationalOperators'):
        index.value+=1
        if E(index,TokenSet):
            if REC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="]" or TokenSet[index.value].CP=="EQUALITY" or TokenSet[index.value].CP=="AND" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")"):
        return True
        
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    False
    

def E(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or  TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if T(index,TokenSet):
            if EC(index,TokenSet):
                return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def EC(index,TokenSet):
    if(TokenSet[index.value].CP == 'MathPM'):
        index.value+=1
        if T(index,TokenSet):
            if EC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="]" or TokenSet[index.value].CP=="RelationalOperators" or TokenSet[index.value].CP=="EQUALITY" or TokenSet[index.value].CP=="AND" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")"):
        return True
        
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False


def T(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" or TokenSet[index.value].CP=="IntegerConstant" or TokenSet[index.value].CP=="StringConstant" or TokenSet[index.value].CP=="DecimalConstant" or TokenSet[index.value].CP== "(" or  TokenSet[index.value].CP== 'NOT' or TokenSet[index.value].CP== "this"):
        if F(index,TokenSet):
            if TC(index,TokenSet):
                return True
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def TC(index,TokenSet):
    if(TokenSet[index.value].CP == 'MathMDM'):
        index.value+=1
        if F(index,TokenSet):
            if TC(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="]" or TokenSet[index.value].CP=="MathPM" or TokenSet[index.value].CP=="RelationalOperators" or TokenSet[index.value].CP=="EQUALITY" or TokenSet[index.value].CP=="AND" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")" or TokenSet[index.value].CP=="}"):
        return True
        
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def F(index,TokenSet):
    if (TokenSet[index.value].CP == "Id"):
        if IDF(index,TokenSet):
            return True
    elif  TokenSet[index.value].CP=="IntegerConstant":
        index.value+=1 
        return True
    elif  TokenSet[index.value].CP=="StringConstant":
        index.value+=1 
        return True
    elif  TokenSet[index.value].CP=="DecimalConstant":
        index.value+=1 
        return True
    elif  TokenSet[index.value].CP=="(":
        index.value+=1
        if OE(index,TokenSet):
            if TokenSet[index.value].CP==")":
                index.value+=1
                return True
    elif TokenSet[index.value].CP=="NOT":
        index.value+=1
        if F(index,TokenSet):
            return True
    elif TokenSet[index.value].CP=="this":
        index.value+=1
        if IDF(index,TokenSet):
            return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def IDF(index,TokenSet):
    if (TokenSet[index.value].CP == "Id" ):
        index.value+=1
        if IDF2(index,TokenSet):
            return True

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def IDF2(index,TokenSet):
    if(TokenSet[index.value].CP=="Dot"):
        if (dot(index,TokenSet) ):
            if IDF2(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP == "[" ):
        index.value+=1
        if OE(index,TokenSet):
            if TokenSet[index.value].CP == "]":
                index.value += 1
                if dot(index,TokenSet):
                    return True
    elif (TokenSet[index.value].CP == "(" ):
        if params(index,TokenSet):
            return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP == "MathMDM" or TokenSet[index.value].CP == "MathPM" or TokenSet[index.value].CP == "RelationalOperators" or TokenSet[index.value].CP == "EQUALITY" or TokenSet[index.value].CP == "AND" or TokenSet[index.value].CP == "OR" or TokenSet[index.value].CP == "," or TokenSet[index.value].CP == "Terminator" or TokenSet[index.value].CP == ")" or TokenSet[index.value].CP == "]"):
        return True 
    
    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False

def dot(index,TokenSet):
    if (TokenSet[index.value].CP == "Dot" ):
        index.value+= 1
        if TokenSet[index.value].CP == "Id":
            index.value+=1
            if IDF2(index,TokenSet):
                return True
    elif (TokenSet[index.value].CP=="}" or TokenSet[index.value].CP=="MathMDM" or TokenSet[index.value].CP=="MathPM" or TokenSet[index.value].CP=="RelationalOperators" or TokenSet[index.value].CP=="EQUALITY" or TokenSet[index.value].CP=="AND" or TokenSet[index.value].CP=="OR" or TokenSet[index.value].CP=="," or TokenSet[index.value].CP=="Terminator" or TokenSet[index.value].CP==")" or TokenSet[index.value].CP=="]" ):
        return True       

    print("Invalid syntax @ " + TokenSet[index.value].LN + " " + TokenSet[index.value].CP)
    return False
    

index=Index()
SyntaxAnalyzer(index, TokenSet)
