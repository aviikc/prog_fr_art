class Dinosaur:
    def __init__(self, name: str, legs: int) -> None:
        self.name = name
        self.legs = legs

    def sayName(self) -> str:
        return self.name
    
    def sayLegs(self) -> str:
        return self.legs