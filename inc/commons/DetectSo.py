import platform 

class DetectSo():
    
    @staticmethod
    def getSo(self):
        self.plt = platform.system()
        return self.plt