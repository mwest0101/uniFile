import os

class SeekString():
    posFound=0
    stringSource=""
    case=True
    firstPos=0
    bandLastPos=0        
    firstStrLen=""
    lastStrLen=""
    
    @classmethod
    def init(cls):
        cls.restPos()

    @classmethod
    def setStrSource(cls,data):
        cls.stringSource=data
        return cls.stringSource

    @classmethod
    def resetPosAndLen(cls):
        cls.firstPos=0
        cls.lastPos=0        
        cls.firstStrLen=0
        cls.lastStrLen=0
    
    @classmethod
    def restPos(cls):
        cls.posFound=0
        cls.resetPosAndLen()                

    @classmethod
    def getPos(cls):
        return cls.posFound  

    @classmethod
    def setPos(cls,value):
        cls.posFound=value
        return cls.posFound
    @classmethod
    def getFirstPos(cls):
        return cls.firstPos
      
    @classmethod
    def getLastPos(cls):
        return cls.lastPos
 
    @classmethod
    def getFirstStrLen(cls):
        return cls.firstStrLen
      
    @classmethod
    def getLastStrLen(cls):
        return cls.lastStrLen

    @classmethod
    def setCaseSensTrue(cls):
        cls.case=True
    
    @classmethod
    def setCaseSensFalse(cls):
        cls.case=False        
    

    @classmethod
    def find(cls,str):
        strSource=cls.stringSource
        strToSeek=str
        posFoundLocal=0 
        if (cls.case==False):
            strSource=strSource.upper()
            strToSeek=strToSeek.upper()
        posFoundLocal=strSource.find(strToSeek,(cls.posFound+1))
        return posFoundLocal


    @classmethod
    def findAndSet(cls,str):
        cls.setPos(cls.find(str))
        return cls.posFound
    

    @classmethod
    def seekAndSetPosAndLen(cls,arrayStr,cont):
        bandFound=True
        if (cont==(-1)):
            cls.lastPos=cls.find(arrayStr)            
            cls.lastStrLen=len(arrayStr)
        else:
            cls.lastPos=cls.find(arrayStr[cont])            
            cls.lastStrLen=len(arrayStr[cont])

        if(cls.firstPos==0):
            cls.firstPos=cls.lastPos
            cls.firstStrLen=cls.lastStrLen
        
        if(cls.lastPos==(-1)):             
               bandFound=False

        cls.setPos(cls.lastPos)
        return bandFound

    # Return if is found all components of a array in a string by array order 
    # return [boolean, firstPosFound,lengthString,lastPosFound,lenghtString]
    @classmethod  
    def seekArrayOfStrs(cls,arrayStr):
        bandFound=True
        # bandFoundOne=False
        cont=0
        cls.resetPosAndLen()
        if (type(arrayStr) is str):
            bandFound=cls.seekAndSetPosAndLen(arrayStr,(-1))            
        else:
            while (cont<len(arrayStr) and bandFound ):
                bandFound=cls.seekAndSetPosAndLen(arrayStr,cont)                           
                cont=cont+1         
        return [bandFound,cls.firstPos,cls.firstStrLen,cls.lastPos,cls.lastStrLen]


    @classmethod  
    def seekArrayOfStrsLestPos(cls,arrayStr):
        bandFound=False
        
        cont=0
        cls.resetPosAndLen()

        if (type(arrayStr) is str):
            cls.lastPos=cls.find(arrayStr)    
            cls.lastStrLen=len(arrayStr)
            cls.firstPos=cls.lastPos
            cls.firstStrLen=cls.lastStrLen
            if(cls.lastPos!=(-1)):             
                bandFound=True            
        else:
            while (cont<len(arrayStr)):
                cls.lastPos=cls.find(arrayStr[cont])            
                cls.lastStrLen=len(arrayStr[cont])                
                if((cls.firstPos==0) or (cls.lastPos<cls.firstPos)):
                    cls.firstPos=cls.lastPos
                    cls.firstStrLen=cls.lastStrLen                              
                if(cls.lastPos!=(-1)):
                    bandFound=True                                  
                cont=cont+1

        return [bandFound,cls.firstPos,cls.firstStrLen,cls.lastPos,cls.lastStrLen]


    
     