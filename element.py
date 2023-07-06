#badger
class Element:
    def __init__(self, name:str, abbreviation:str, type:str, atomic_num:int, atomic_mass:float):
        self.name = name
        self.abbreviation = abbreviation
        self.type = type
        self.atomic_num = atomic_num
        self.atomic_mass = atomic_mass
    def __str__(self):
        return "name: "+self.name+"\nabbreviation: "+self.abbreviation+"\ntype: "+self.type+"\natomic_number: "+str(self.atomic_num)+"\natomic_mass: "+str(self.atomic_mass)