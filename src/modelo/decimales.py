class Decimal():
    def __init__(self) -> None:
        pass

    def comprobar(self, num):
        if len(num) <= 0:
            return ""
        
        if num[0].isdigit():
            return num[0] + self.comprobar(num[1:len(num)])
        
        return ""