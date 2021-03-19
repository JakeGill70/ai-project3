import json
from KnowledgeBase import KnowledgeBase


class Relationships:

    def __init__(self):
        self.kb = KnowledgeBase()
        with open("relationships.json") as f:
            d = json.loads(f.read())
            self.parents = d['parent']

    def isMale(self, x):
        raise NotImplementedError

    def isFemale(self, x):
        raise NotImplementedError

    def isParent(self, x, y):
        return {x: y} in self.parents

    def isFather(self, x, y):
        raise NotImplementedError

    def isMother(self, x, y):
        raise NotImplementedError

    def isSibling(self, x, y):
        raise NotImplementedError

    def isSpouse(self, x, y):
        raise NotImplementedError

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
