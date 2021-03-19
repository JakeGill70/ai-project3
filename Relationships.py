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

# Parent
    def isParent(self, x, y):
        return {x: y} in self.parents

# Father
    def isFather(self, x, y):
        return self.isParent(x, y) and self.isMale(y)

# Mother
    def isMother(self, x, y):
        return self.isParent(x, y) and self.isFemale(y)

# Sibling
    def isSibling(self, x, y):
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(x, z) and self.isParent(y, z)):
                return True
        return False

# Spouse
    def isSpouse(self, x, y):
        for char in self.kb.characters:
            z = char["Name"]
            if(self.isParent(z, x) and self.isParent(z, y)):
                return True
        return False

# Niece
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

# Nephew
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

# Cousin
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

# Sister
    def isSister(self, x, y):
        return self.isSibling(x, y) and self.isFemale(y)

# Brother
    def isBrother(self, x, y):
        return self.isSibling(x, y) and self.isMale(y)

# Grandparent
    def isGrandparent(self, x, y):
        raise NotImplementedError()

# Grandfather
    def isGrandfather(self, x, y):
        raise NotImplementedError()

# Grandmother
    def isGrandmother(self, x, y):
        raise NotImplementedError()

# Great-Grandparent
    def isGreatGrandparent(self, x, y):
        raise NotImplementedError()

# Great-Grandmother
    def isGreatGrandmother(self, x, y):
        raise NotImplementedError()

# Great-Grandfather
    def isGreatGrandfather(self, x, y):
        raise NotImplementedError()
