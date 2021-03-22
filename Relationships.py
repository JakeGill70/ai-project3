import json
from KnowledgeBase import KnowledgeBase


class Relationships:

    def __init__(self):
        self.kb = KnowledgeBase()
        with open("relationships.json") as f:
            d = json.loads(f.read())
            self.parents = d['parent']

        self.dispatchFunction = {
            "Spouse": self.isSpouse,
            "Sibling": self.isSibling,
            "Sister": self.isSister,
            "Brother": self.isBrother,
            "Niece": self.isNiece,
            "Nephew": self.isNephew,
            "Cousin": self.isCousin,
            "Parent": self.isParent,
            "Mother": self.isMother,
            "Father": self.isBrother,
            "Grandparent": self.isGrandparent,
            "Grandfather": self.isGrandfather,
            "Grandmother": self.isGrandmother,
            "Great-Grandparent": self.isGrandparent,
            "Great-Grandfather": self.isGreatGrandfather,
            "Great-Grandmother": self.isGreatGrandmother
        }

    def getCharacters(self):
        return self.kb.characters

    def findCharacter(self, name):
        try:
            return [char for char in self.getCharacters() if char["Name"] == name][0]
        except IndexError:
            # An index error occurs if the first list is empty, no element [0].
            # If the list is empty, then no character has that name, and we may
            # just return None.
            return None

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
        # Siblings is true if x and y share any parent
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(x, z) and self.isParent(y, z)):
                return True
        return False

# Spouse
    def isSpouse(self, x, y):
        # Spouce is true if x and y share any child
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(z, x) and self.isParent(z, y)):
                return True
        return False

# Niece
    def isNiece(self, x, y):
        # Get y's parents
        yParents = []
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(y, z)):
                yParents.append(z)

        # Determine if y's parents are siblings of x
        yParentIsSibling = False
        for z in yParents:
            if(self.isSibling(x, z)):
                yParentIsSibling = True
                break

        # Return true if y's parents are siblings of x, and x is female
        isNiece = yParentIsSibling and self.isFemale(y)

        return isNiece

# Nephew
    def isNephew(self, x, y):
        # Get y's parents
        yParents = []
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(y, z)):
                yParents.append(z)

        # Determine if y's parents are siblings of x
        yParentIsSibling = False
        for z in yParents:
            if(self.isSibling(x, z)):
                yParentIsSibling = True
                break

        # Return true if y's parents are siblings of x, and x is male
        isNephew = yParentIsSibling and self.isMale(y)

        return isNephew

# Cousin
    def isCousin(self, x, y):
        # Get both x's and y's parent
        xParents = []
        yParents = []
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(x, z)):
                xParents.append(z)
            if(self.isParent(y, z)):
                yParents.append(z)

        # Determine if any of x's parents are siblings to any of y's parents
        parentsAreSiblings = False
        for xp in xParents:
            for yp in yParents:
                if(self.isSibling(xp, yp)):
                    parentsAreSiblings = True

        # x and y are 1st cousins if either if any parent between x and y are siblings
        return parentsAreSiblings

# Sister
    def isSister(self, x, y):
        return self.isSibling(x, y) and self.isFemale(y)

# Brother
    def isBrother(self, x, y):
        return self.isSibling(x, y) and self.isMale(y)

# Grandparent
    def isGrandparent(self, x, y):
        # Get x's parents
        xParents = []
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isParent(x, z)):
                xParents.append(z)

        # Return true if either of x's parents has y for a parent
        for xParent in xParents:
            if(self.isParent(xParent, y)):
                return True

        # Return false if none of x's parents has y for a parent
        return False

# Grandfather
    def isGrandfather(self, x, y):
        return self.isGrandparent(x, y) and self.isMale(y)

# Grandmother
    def isGrandmother(self, x, y):
        return self.isGrandparent(x, y) and self.isFemale(y)

# Great-Grandparent
    def isGreatGrandparent(self, x, y):
        # Get x's grandparents
        xGrandParents = []
        for char in self.getCharacters():
            z = char["Name"]
            if(self.isGrandparent(x, z)):
                xGrandParents.append(z)

        # Return true if any of x's grandparents has y as a parent
        for xGrandParent in xGrandParents:
            if(self.isParent(xGrandParent, y)):
                return True

        # Return false if none of x's grandparents has y as a parent
        return False

# Great-Grandmother
    def isGreatGrandmother(self, x, y):
        return self.isGreatGrandparent(x, y) and self.isFemale(y)

# Great-Grandfather
    def isGreatGrandfather(self, x, y):
        return self.isGreatGrandparent(x, y) and self.isMale(y)
