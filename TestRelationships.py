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


if __name__ == '__main__':
    unittest.main()
