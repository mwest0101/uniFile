import os
from inc.app.lang import *

class ReadDirs():
    def readDirs(self,pathDirs):
        for path, subdirs, files in os.walk(pathDirs):
            for fileName in files:
                    print ('in path ' +str(path)+"\\"+str(fileName))
