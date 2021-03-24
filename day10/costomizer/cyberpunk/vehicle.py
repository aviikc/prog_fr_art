'''
class Vehicle -> constructor (brand(string) model[string] color[tuple] electric[bool]) methods (brand, model, color, electric)
'''

class Vehicle:
    def __init__(self, brand: str, model: str, color: tuple, elec: bool) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.elec = elec
        
    def getBrand(self):
        return self.brand
             
    def getModel(self):
        return self.model
                
    def getColor(self):
        return self.color
    
    def getEle(self):
        return self.elec