from inc.app.config_inc import *

class StrNormalize():
    so="WIN"

    @classmethod
    def init(cls,so):
        cls.so=so

    @classmethod
    def replaceSlash(cls,stringIn):
        if(cls.so=="WIN"):                        
            stringIn=stringIn.replace("/", "\\") 
            stringIn=stringIn.replace("\\\\", "\\")           
        else:                        
            stringIn=stringIn.replace("\\", "/")
            stringIn=stringIn.replace("//", "/")
        
        return stringIn

