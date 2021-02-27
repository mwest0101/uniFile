from inc.app.config_inc import *
from inc.app.info.info_strings import *
from inc.app.lang.en_strings import *
# from inc.commons.Debug import *
from inc.commons.ReadFile import *
from inc.commons.SeekString import *
from inc.app.Functions import *
from inc.app.JsonParams import *



print(CONST_INTRO)
pathToFile=StrNormalize.replaceSlash(JsonParams.getPath()+"/"+JsonParams.getFile())
fileStr=ReadFile.read(pathToFile)
SeekString.init()
SeekString.setStrSource(fileStr)



print(Functions.getAllStringInFileFromJsonDef(fileStr))
print("---------------------------------------------------------------------")


# Functions.orderByIdReversed()
# print(Functions.orderByIdReversed())
# print("---------------------------------------------------------------------")


# print(Functions.orderBy("id"))
# print("---------------------------------------------------------------------")

# print(Functions.orderBy("strFound"))
# print("---------------------------------------------------------------------")

# print(Functions.orderBy("posFound"))
# print("---------------------------------------------------------------------")
