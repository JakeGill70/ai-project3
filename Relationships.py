import json
from KnowledgeBase import KnowledgeBase


class Relationships:

    def __init__(self):
        self.kb = KnowledgeBase()
        with open("relationships.json") as f:
            d = json.loads(f.read())
            self.parents = d['parent']

    def findCharacter(self, name):
        return [char for char in self.kb.characters if char["Name"] == name][0]

    def isMale(self, x):
        return self.findCharacter(x)["Gender"] == "Male"

    def isFemale(self, x):
        return self.findCharacter(x)["Gender"] == "Female"

    def isParent(self, x, y):
        return {x: y} in self.parents

    def isFather(self, x, y):
        return self.isParent(x, y) and self.isMale(y)

    def isMother(self, x, y):
        return self.isParent(x, y) and self.isFemale(y)

    def isSibling(self, x, y):
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(x, z) and self.isParent(y, z)):
                return True
        return False

    def isSpouse(self, x, y):
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(z, x) and self.isParent(z, y)):
                return True
        return False

    def isSister(self, x, y):
        raise NotImplementedError

    def isBrother(self, x, y):
        raise NotImplementedError

    def isNeice(self, x, y):
        raise NotImplementedError

    def isNepthew(self, x, y):
        raise NotImplementedError

    def isNiece(self, x, y):
        raise NotImplementedError

    def isCousin(self, x, y):
        raise NotImplementedError
