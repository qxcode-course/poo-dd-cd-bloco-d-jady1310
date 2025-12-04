class Fone:
    def __init__(self, id:str, number:str):
        self.__id=id
        self.__number=number
    
    def isValid(self) -> bool:
        valid = "0123456789()."
        return all(c in valid for c in self.__number)
    
    def getId(self)->str:
        return self.__id
    def getNumber(self)->str:
        return self.__number
    def toString(self) -> str:
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name:str=" "):
        self.__favorited=False
        self.__name=name
        self.__fones:list[Fone]=[]
    
    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print(f"fail: fone invalido '{number}'")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: indice invalido")
    
    def toogleFavorited(self) -> None:
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited
    
    def getName(self) -> str:
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name
    
    def getFones(self) -> list:
        return self.__fones
    
    def toString(self) -> str:
        prefix = "@" if self.__favorited else ""
        fones_str = ", ".join(fone.toString() for fone in self.__fones)
        return f"- {prefix}{self.__name} [{fones_str}]"
    
def main():
    