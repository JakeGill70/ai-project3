from Relationships import Relationships
import sys


def makeRelationshipOutput(relationships, fileName=None):

    FILE_OUTPUT = open(fileName, "w") if fileName else None

    if(FILE_OUTPUT):
        normalOutput = sys.stdout
        sys.stdout = FILE_OUTPUT

    print("Relationship_Name,Person_x,Person_Y")

    for r in relationships.dispatchFunction.keys():
        for personX in relationships.getCharacters():
            x = personX["Name"]
            for personY in relationships.getCharacters():
                y = personY["Name"]

                related = relationships.dispatchFunction[r](x, y)
                if(related):
                    print(r, x, y)

    if(FILE_OUTPUT):
        FILE_OUTPUT.close()
        sys.stdout = normalOutput


def main():
    relationships = Relationships()
    makeRelationshipOutput(relationships, "RelationshipOutput.csv")


main()
