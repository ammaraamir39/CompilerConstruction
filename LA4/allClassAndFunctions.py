class SymbolTable:
    def __init__(self):
        self.name = None
        self.type=None
        self.scope=None

class FunctionTable:
    def __init__(self):
        self.name=None
        self.type=None

class ClassTable:
    def __init__(self):
        self.name=None
        self.type=None
        self.parent=None
        self.classReference=None

class ClassDataTable:
    def __init__(self):
        self.name=None
        self.type=None
        self.accessModifier=None
        self.typeModifier=None
    
class TemporaryObject:
    def __init__(self):
        self.name= None
        self.type=None
        self.operator=None
        self.argumentedType=[]
        self.argumentName=[]


