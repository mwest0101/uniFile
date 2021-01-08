# ////////////////////////////////////////////////////////////
# ------ INCLUDES --------------------------------------------
from inc.commons.SeekString import *
from inc.commons.ReadJson import *
from inc.app.config_inc import *

# ------------------------------------------------------------


class JsonParams():
    one_param = ""
    strToSeek = ""
    file = ""
    path = ""
    order = ""
    typeFile = ""
    so = ""
    strToSeek = ""
    countParam=-1
    amountParam=0
    eLine=[]
    eLineKey=[]
    countEline=0
    keyParams=[]

    @classmethod
    def loadFile(cls, fileJson):
        ReadJson.openFile(fileJson)
        cls.file = ReadJson.getElement("main")
        cls.path = ReadJson.getElement("path")
        cls.order = ReadJson.getElement("order")
        cls.typeFile = ReadJson.getElement("type")
        cls.debug = ReadJson.getElement("debug")        
        cls.so = ReadJson.getElement("so")
        ReadJson.getAndSet(cls.typeFile)
        cls.eLine = ReadJson.getElement("endLine")        
        cls.strToSeek = ReadJson.getAndSet("seek")
        cls.amountParam=len(cls.strToSeek)
        for key in cls.strToSeek.keys():
            cls.keyParams.append(key)
        
        for key in cls.eLine.keys():
            cls.eLineKey.append(key)

    @classmethod
    def getFile(cls):
        return cls.file

    @classmethod
    def getPath(cls):
        return cls.path

    @classmethod
    def getOrder(cls):
        return cls.order

    @classmethod
    def getTypeFile(cls):
        return cls.typeFile

    @classmethod
    def getSo(cls):
        return cls.so
    
    @classmethod
    def getDebug(cls):
        return cls.debug
    
    @classmethod
    def getParamsEli(cls):
        result=[]
        for data in cls.eLine:
            result.append(cls.eLine[data])
        return result
    
    @classmethod
    def getParamEli(cls,nume):
        return cls.eLine[cls.eLineKey[cls.countEline]]
    
    @classmethod
    def getParamOneEli(cls):
        result=0
        if(cls.countEline<len(cls.getParamsEli())):
             result=cls.getParamEli(cls.countEline)
             cls.countEline=cls.countEline+1
        else:
             cls.countEline=0
             result=0
        return result

    @classmethod
    def getStrToSeek(cls):
        return cls.strToSeek

    @classmethod
    def getParam(cls, number):
        cls.one_param = cls.strToSeek[number]
        return cls.one_param

    @classmethod
    def getParamSpaces(cls):
        return cls.one_param["chSpaces"]

    @classmethod
    def getParamCSens(cls):
        if (cls.one_param["caseSens"] == "true"):
            SeekString.setCaseSensTrue()
        else:
            SeekString.setCaseSensFalse()

        return cls.one_param["caseSens"]

    @classmethod
    def getParamExt(cls):
        return cls.one_param["ext"]

    @classmethod
    def getParamStr(cls):
        return cls.one_param["str"]

        # return {"change":sChange,"sens":cSens,"ext":ext,"str":strToSeek}
    

    @classmethod
    def getParamFromJson(cls,number):

        param = cls.getParam(number)
        param_change = cls.getParamSpaces()
        param_sens = cls.getParamCSens()
        param_ext = cls.getParamExt()
        param_str = cls.getParamStr()
        

        if (param_sens == "true"):
            SeekString.setCaseSensTrue()
        else:
            SeekString.setCaseSensFalse()

        return {"param":param,"change":param_change,"sens":param_sens,"ext":param_ext,"str":param_str}        
    
    @classmethod
    def getCountParam(cls):
        return cls.countParam

    @classmethod
    def getKeys(cls):
        return cls.keyParams

    @classmethod
    def getValuefromKey(cls):
        return cls.keyParams[cls.countParam]

    @classmethod
    def getOneParam(cls):        
        result=""
        if(cls.countParam<(cls.amountParam-1)):
            cls.countParam=cls.countParam+1
            result=cls.getParamFromJson(cls.getValuefromKey())                        
            return result
        else:
            cls.countParam=0
            return 0


    
