from inc.app.config_inc import *

from inc.commons.StrNormalize import *
from inc.commons.SeekString import *
from inc.commons.Debug import *
from inc.app.lang import *

class Functions():
    resultArrayPath=[]
    countFounds=0
    @classmethod                
    def getPathToFile(cls,path,fileStr,results0,results1,ext):
        result=path+"/"+fileStr[(results0[3]+results0[4]):results1[1]]+"."+ext        
        result=StrNormalize.replaceSlash(result)
        return result
    
    @classmethod
    def getStrOrArrayIfSpaces(cls,spaceChange,str):
        if (spaceChange=="true"):
            result=str.split()            
        else:            
            result=str
        return result
    
    @classmethod
    def seekStr(cls,fileStr):
        oneStrFile=JsonParams.getParamStr().split("{file}") 
        part0=cls.getStrOrArrayIfSpaces(JsonParams.getParamSpaces(),oneStrFile[0])
        part1=cls.getStrOrArrayIfSpaces(JsonParams.getParamSpaces(),oneStrFile[1])
        results0=SeekString.seekArrayOfStrs(part0)
        results1=SeekString.seekArrayOfStrs(part1)
        # endLine=JsonParams.getParamsEli()
        # resultEnline=SeekString.seekArrayOfStrs(endLine)

        # if((results0[0]==True) and (results1[0]==True) and (results1[1]<resultEnline[1])):            
        if((results0[0]==True) and (results1[0]==True)):            
            result={"id":cls.countFounds,"strFound":JsonParams.getValuefromKey(),"posFound":SeekString.getLastPos(),"strFile":cls.getPathToFile(JsonParams.getPath(),fileStr,results0,results1,JsonParams.getParamExt())}
            cls.countFounds=cls.countFounds+1
        else:
            result=0          
            # Debug.print("--> Not found , the string:  ["+JsonParams.getValuefromKey()+"] :" +JsonParams.getParamStr())
        
        return result
     
    @classmethod   
    def getArrayPaths(cls,fileStr):
        
        seekResult=1
        while (seekResult!=0):
            seekResult=cls.seekStr(fileStr)
            if (seekResult!=0):
                cls.resultArrayPath.append(seekResult)
                
                # print (seekResult)
        return cls.resultArrayPath
        
    @classmethod
    def getResultArrayPath(cls):
        return cls.resultArrayPath
        
    @classmethod
    def getAllStringInFileFromJsonDef(cls,fileStr):
        cls.countFounds=0
        result=JsonParams.getOneParam()
        while (result!=0):
            cls.getArrayPaths(fileStr)       
            result=JsonParams.getOneParam()
        Debug.print(Functions.getResultArrayPath())
        return cls.getResultArrayPath()
    
    @classmethod
    def orderByIdReversed(cls):
        array1Temp=[]
        data=[]
        for data in reversed(cls.resultArrayPath):
            array1Temp.append(data)
        cls.resultArrayPath=array1Temp
        return cls.resultArrayPath
            
    @classmethod
    def orderBy(cls,strOrder):
        print ("orderBy ="+strOrder)
        array1Temp=cls.resultArrayPath
        pos2=0        
        for cont in range(len(array1Temp)):                        
            for cont2 in range((len(array1Temp)-(cont+1))):     
                pos2=(cont+1)+cont2                   
                if(array1Temp[cont][strOrder]>array1Temp[pos2][strOrder]):                   
                   tempVal=array1Temp[cont]
                   array1Temp[cont]=array1Temp[pos2]
                   array1Temp[pos2]=tempVal       

        cls.resultArrayPath=array1Temp
        return cls.resultArrayPath

    @classmethod
    def orderById(cls):
        cls.orderBy("id")


        
    
