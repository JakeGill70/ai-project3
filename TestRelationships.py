import unittest
from Relationships import Relationships


class TestRelationships(unittest.TestCase):

    def test_parent(self):
        r = Relationships()
        assert r.isParent("Anita", "Paul") == True
        assert r.isParent("Paul", "Anita") == False

    def test_gender(self):
        r = Relationships()
        assert r.isMale("Paul") == True
        assert r.isMale("Anita") == False
        assert r.isFemale("Anita") == True
        assert r.isFemale("Paul") == False

    def test_mother(self):
        r = Relationships()
        assert r.isMother("Anita", "Anne") == True
        assert r.isMother("Anne", "Anita") == False
        assert r.isMother("Anita", "Paul") == False
        assert r.isMother("Anita", "Sam") == False
        assert r.isMother("Paul", "Anita") == False

    def test_father(self):
        r = Relationships()
        assert r.isFather("Anita", "Paul") == True
        assert r.isFather("Paul", "Anita") == False
        assert r.isFather("Anita", "Sam") == False

    def test_sibling(self):
        r = Relationships()
        assert r.isSibling("Anita", "Alex") == True
        assert r.isSibling("Alex", "Anita") == True
        assert r.isSibling("Anita", "Paul") == False
        assert r.isSibling("Anita", "Bill") == False

    def test_spouse(self):
        r = Relationships()
        assert r.isSpouse("Paul", "Anne") == True
        assert r.isSpouse("Anne", "Paul") == True
        assert r.isSpouse("Anita", "Alex") == False
        assert r.isSpouse("Paul", "Anita") == False

    def test_niece(self):
        r = Relationships()
        assert r.isNiece("Tom", "Claire") == True
        assert r.isNiece("Max", "Alex") == False
        assert r.isNiece("Claire", "Tom") == False
        assert r.isNiece("Anita", "Alex") == False
        assert r.isNiece("Anita", "Joe") == False


if __name__ == '__main__':
    unittest.main()
