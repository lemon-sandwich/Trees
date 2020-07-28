# ------------------------------------------------ #
# Choose Name or Designation or Both to Print in a Tree

class Tree:
    def __init__(self,data,designation):
        self.data = data
        self.designation = designation
        self.parent = None
        self.children = []
        
    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def getlevel(self):
        level = 0
        if self is not None:
            p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print(self,selection):
        prefix = ' ' * self.getlevel() * 3
        prefix += "|--"
        if selection == '1':
            print(prefix + self.data)
        elif selection == '2':
            print(prefix + self.designation)
        elif selection == '3':
            print(prefix + self.data, '(',self.designation,')')
        
        if self.children:
            for child in self.children:
                child.print(selection)
        

def buildproducttree():
    Nilupul = Tree("Nilupul","CEO")
    Chinmay = Tree("Chinmay","CTO")
    Gels = Tree("Gels","HR Head")
    Vishwa = Tree("Vishwa","Infrastructure Head")
    Dhaval = Tree("Dhaval","Cloud Manager")
    Abhijit = Tree("Abhijit","App Manager")
    Aamir = Tree("Aamir","Application Head")
    Peter = Tree("Peter","Recruitment Manager")
    Waqas = Tree("Waqas","Policy Manager")
    Nilupul.add_child(Gels)
    Nilupul.add_child(Chinmay)
    Vishwa.add_child(Dhaval)
    Vishwa.add_child(Abhijit)
    Chinmay.add_child(Vishwa)
    Chinmay.add_child(Aamir)
    Gels.add_child(Peter)
    Gels.add_child(Waqas)
    selection = '0'
    while selection != '-1':
        print("1. Name")
        print("2. Designation")
        print("3. Both")
        selection = input("Choose: ")
        if selection != '-1':
            print("\n\n\n\n\n")
            Nilupul.print(selection)
            print("\n\n\n\n\n")

if __name__ is '__main__':
    buildproducttree()
    input("Press Any Other Key To Start The Other Exercise\n")
    
    


# ---------------------------------------------------------------- #
# Taking Level As Input To Print

class Tree2:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
        
    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def getlevel(self):
        level = 0
        if self is not None:
            p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print(self,level):
        if self.getlevel() < level:
            prefix = ' ' * self.getlevel() * 3
            prefix += "|--"
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print(level)


def build_location_tree():
    Global = Tree2("Global")
    India = Tree2("India")
    Gujrat = Tree2("Gujrat")
    Ahmedabad = Tree2("Ahmedabad")
    Baroda = Tree2("Baroda")
    Karnataka = Tree2("Karnataka")
    Bangluru = Tree2("Bangluru")
    Mysore = Tree2("Mysore")
    USA = Tree2("USA")
    NewJersey = Tree2("New Jersey")
    Princeton = Tree2("Princeton")
    Trenton = Tree2("Trenton")
    California = Tree2("California")
    SanFrancisco = Tree2("San Francisco")
    MountainView = Tree2("Mountain View")
    PaloAlto = Tree2("Palo Alto")
    Global.add_child(India)
    Global.add_child(USA)
    India.add_child(Gujrat)
    India.add_child(Karnataka)
    Gujrat.add_child(Ahmedabad)
    Gujrat.add_child(Baroda)
    Karnataka.add_child(Bangluru)
    Karnataka.add_child(Mysore)
    USA.add_child(NewJersey)
    USA.add_child(California)
    NewJersey.add_child(Princeton)
    NewJersey.add_child(Trenton)
    California.add_child(SanFrancisco)
    California.add_child(MountainView)
    California.add_child(PaloAlto)
    level = 0
    while level != -1:
        level = int(input("Level: "))
        print("\n\n\n\n")
        Global.print(level)
        print("\n\n\n\n")

build_location_tree()

