
class Profit:
    
    profit = 0
    
    def __init__(self, val):
        self.val = val
        
        Profit.profit += self.val
        
        
class Debet:
    
    debet = 0
    
    def __init__(self, val):
        self.val = val
        
        Debet.debet += self.val
        
        
class Result:
    
    def __init__(self):
        self.profit = Profit.profit
        self.debet = Debet.debet
        
    def result(self):
        result = self.profit - self.debet
        return result


class Sut:
    
    sut = 0
    
    def __init__(self, val):
        self.val = val
        
        Sut.sut = self.val
        
    #def result(self):
        #result = self.profit - self.debet
        #return result
        
error_s = '--> Неверный ввод!'

def check(s):
    try:
        int(s)
        s = s.lstrip('0')
        if not s: s = 0
    except:
        try:
            float(s)
            #s = s.lstrip('0')
        except:
            s = error_s
    return s
