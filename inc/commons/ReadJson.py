import commentjson
import array
from inc.app.lang.en_strings import *


class ReadJson():

    f = ""
    content = ""
    jsondecoded = ""
    result = ""

    @classmethod
    def openFile(self, pathAndFile):
        try:
            self.f = open(pathAndFile, "r")
            self.content = self.f.read()
            self.jsondecoded = commentjson.loads(self.content)
            self.result = self.jsondecoded
        except:
            print('|||| '+CONST_NO_OPEN_FILE+' ['+pathAndFile+']  |||')

    @classmethod
    def printAll(self):
        print(self.jsondecoded)

    @classmethod
    def getRoot(self):
        return self.jsondecoded

    @classmethod
    def reset(self):
        self.result = self.jsondecoded

    @classmethod
    def setElement(self, array):
        self.result = array

    @classmethod
    def getElement(self, strElement):
        try:
            return self.result[strElement]
        except:
            print('--> El indice "', strElement, '" ¡NO EXISTE!')
            return 0

    @classmethod
    def getAndSet(self, strElement):
        self.result = self.getElement(strElement)
        return self.result

    @classmethod
    def printIndex(self):
        if (self.result):
            for data in self.result:
                print(data)
        else:
            Debug.print(CONST_RDJ_THERE_NO_VALUES_ARRAY)

    @classmethod
    def getIndex(self):
        values = []
        if (self.result):
            for data in self.result:
                values.append(data)
            return values
        else:
            Debug.print(CONST_RDJ_THERE_NO_VALUES_ARRAY)
            return 0

    @classmethod
    def printValues(self):
        if (self.result):
            for data in self.result:
                Debu.print(self.result[data])
        else:
            Debug.print(CONST_RDJ_THERE_NO_VALUES_ARRAY)

    @classmethod
    def getValues(self):
        values = []
        if (self.result):
            for data in self.result:
                values.append(self.result[data])
            return values
        else:
            Debug.print(CONST_RDJ_THERE_NO_VALUES_ARRAY)
            return 0

    @classmethod
    def getArray(self):
        if (self.result):
            return self.result
        else:
            Debug.print(CONST_RDJ_THERE_NO_VALUES_ARRAY)
