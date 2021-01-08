from inc.app.JsonParams import *

class Debug():
    
    @staticmethod
    def print(string):
        if(JsonParams.getDebug()=="true"):
            print (string)
