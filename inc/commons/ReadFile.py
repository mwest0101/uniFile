import os
from inc.commons.Debug import *
from inc.app.lang.en_strings import *

class ReadFile():
    stringResult=""    
    lastOpenFile=""
    lastWriteFile=""

    @classmethod
    def read(cls,pathAndFile):
        result=""
        try:
            f = open(pathAndFile, "r")
            cls.lastOpenFile=pathAndFile
            result=f.read()
            f.close()
            cls.stringResult=result
            return result
        except:
            Debug.print(CONST_NO_OPEN_FILE)
            return 0

    @classmethod
    def write(cls,pathAndFile,text):
        try:
            f = open(pathAndFile, "a")
            cls.lastWrite=pathAndFile
            f.write(text)
            f.close()
        except:
            Debug.print(CONST_NO_OPEN_FILE)
            return 0
            
    @classmethod                
    def getString(cls):
        return cls.stringResult

        