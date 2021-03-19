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

    def isNiece(self, x, y):
        yParents = []
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(y, z)):
                yParents.append(z)

        yParentIsSibling = False
        for z in yParents:
            if(self.isSibling(x, z)):
                yParentIsSibling = True
                break

        isNiece = yParentIsSibling and self.isFemale(y)

        return isNiece

    def isNephew(self, x, y):
        yParents = []
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(y, z)):
                yParents.append(z)

        yParentIsSibling = False
        for z in yParents:
            if(self.isSibling(x, z)):
                yParentIsSibling = True
                break

        isNephew = yParentIsSibling and self.isMale(y)

        return isNephew

    def isCousin(self, x, y):
        xParents = []
        yParents = []
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(x, z)):
                xParents.append(z)
            if(self.isParent(y, z)):
                yParents.append(z)

        parentsAreSiblings = False
        for xp in xParents:
            for yp in yParents:
                if(self.isSibling(xp, yp)):
                    parentsAreSiblings = True

        return parentsAreSiblings

    def isSister(self, x, y):
        return self.isSibling(x, y) and self.isFemale(y)

    def isBrother(self, x, y):
        return self.isSibling(x, y) and self.isMale(y)
