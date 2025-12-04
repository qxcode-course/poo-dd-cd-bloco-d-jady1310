class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number
    
    def isValid(self) -> bool:
        valid = "0123456789()+-"
        return all(c in valid for c in self.__number)
    
    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number
    
    def toString(self) -> str:
        return f"{self.__id}:{self.__number}"
    
    def __str__(self):
        return self.toString()

    


class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited = False
    
    def addFone(self, id: str, number: str) -> None:
        f = Fone(id, number)
        if f.isValid():
            self.__fones.append(f)
    
    def addFoneObj(self, fone: "Fone"):
        if fone.isValid():
            self.__fones.append(fone)

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
    
    def toggleFavorited(self) -> None:
        self.__favorited = not self.__favorited
    
    def isFavorite(self) -> bool:
        return self.__favorited
    
    def getFones(self) -> list:
        return self.__fones
    
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str) -> None:
        self.__name = name
    
    def toString(self) -> str:
        star = "@" if self.__favorited else "-"
        fones = ", ".join(str(f) for f in self.__fones)
        return f"{star} {self.__name} [{fones}]"
    
    def __str__(self):
        return self.toString()


class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []
    
    def findPosByName(self, name: str) -> int:
        for i, c in enumerate(self.__contacts):
            if c.getName() == name:
                return i
        return -1
    
    def addContact(self, name: str, fones: list[Fone]) -> None:
        pos = self.findPosByName(name)
        if pos != -1:
            contact = self.__contacts[pos]
            for f in fones:
                contact.addFoneObj(f)
            return
        
        new_contact = Contact(name)
        for f in fones:
            new_contact.addFoneObj(f)
        self.__contacts.append(new_contact)
        self.__contacts.sort(key=lambda c: c.getName())
    
    def getContact(self, name: str):
        pos = self.findPosByName(name)
        return self.__contacts[pos] if pos != -1 else None
    
    def rmContact(self, name: str) -> None:
        pos = self.findPosByName(name)
        if pos != -1:
            self.__contacts.pop(pos)
    
    def search(self, pattern: str) -> list[Contact]:
        pattern = pattern.lower()
        result = []

        for c in self.__contacts:
            if pattern in c.getName().lower():
                result.append(c)
                continue
            for f in c.getFones():
                if (pattern in f.getId().lower() or pattern in f.getNumber().lower()):
                    result.append(c)
                    break
        
        return result
    
    def getFavorited(self) -> list[Contact]:
        return [c for c in self.__contacts if c.isFavorite()]
    
    def getContacts(self) -> list[Contact]:
        return self.__contacts
    
    def toString(self) -> str:
        return "\n".join(str(c) for c in self.__contacts)
    
    def __str__(self):
        return self.toString()
    
    
def main():
    agenda=Agenda()
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print(f"${line}")

        if args[0] =="end":
            break
        elif args[0]== "add":
            nome=args[1]
            listFones=[]
            for i in range(2,len(args)):
                numero=args[i]
                id,number=numero.split(":")
                telefone=Fone(id,number)
                listFones.append(telefone)
            agenda.addContact(nome,listFones)
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "rmFone":
            nome = args[1]
            indice = int(args[2])
            contato = agenda.getContact(nome)
            if contato:
                contato.rmFone(indice)
        elif args[0] == "rm":
            name = args[1]
            agenda.rmContact(name)
        elif args[0] == "search":
            pattern = args[1]
            for contato in agenda.search(pattern):
                print(contato)
        elif args[0] == "tfav":
            name = args[1]
            contato = agenda.getContact(name)
            if contato:
                contato.toggleFavorited()
        elif args[0] == "favs":
            for favoritos in agenda.getFavorited():
                print(favoritos)

        else:
            print("fail: comando invalido")
main()