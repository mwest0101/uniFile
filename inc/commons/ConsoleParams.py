import sys
from inc.commons.Debug import *
from inc.app.lang import *

class ConsoleParams():

    @staticmethod
    def printParams():
        cont=0
        for parameter in sys.argv:
            cont=cont+1
            Debug.print("| Parameter "+str(cont)+" = "+parameter+" |")

    
    @staticmethod
    def getParams():
        return sys.argv

    @staticmethod
    def getOneParam(indice):
        return sys.argv[indice]
