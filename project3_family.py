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


def processInput(rawInput):
    # Define output values
    relationship = None
    personX = None
    personY = None

    if(rawInput.lower().startswith("is ")):
        # NLP input
        request = rawInput.split(" ")
        if(len(request) == 4):
            # Ignore request[0] because it is "is"
            # Ensure first letter is capitalized
            personY = request[1].capitalize()
            # Remove 's if necessary
            # Ensure first letter is capitalized
            personX = request[2][:-2].capitalize() if request[2].endswith("'s") else request[2].capitalize()
            # Remove ? if necessary
            # Ensure first letter is capitalized
            relationship = request[3][:-1].capitalize() if request[3].endswith("?") else request[3].capitalize()
    else:
        # Normal input
        # Request format: "RELATIONSHIP PERSON_X PERSON_Y"
        request = rawInput.split(" ")
        if(len(request) == 3):
            # Ensure that all 3 are capitalized
            relationship = request[0].capitalize()
            personX = request[1].capitalize()
            personY = request[2].capitalize()

    # Return the results as a dictionary because tuples cause troubles
    return {"relationship": relationship, "x": personX, "y": personY}


def verifyInput(processedInput, relationships):
    # Get the values from processedInput()'s dicionary
    relationship = processedInput["relationship"]
    personX = processedInput["x"]
    personY = processedInput["y"]

    # Assume the input is valid until proven otherwise
    isValidInput = True

    # Is the relationship defined?
    if(relationship not in relationships.dispatchFunction.keys()):
        print(
            f"Relationship '{relationship}' is not defined. Relationship must be: {list(relationships.dispatchFunction.keys())}",
            file=sys.stderr)
        isValidInput = False

    # Does person_x exist?
    if(not relationships.findCharacter(personX)):
        print(
            f"Person '{personX}' is not defined. Person X must be: {[c['Name'] for c in relationships.getCharacters()]}",
            file=sys.stderr)
        isValidInput = False

    # Does person_y exist?
    if(not relationships.findCharacter(personY)):
        print(
            f"Person '{personY}' is not defined. Person X must be: {[c['Name'] for c in relationships.getCharacters()]}",
            file=sys.stderr)
        isValidInput = False

    return isValidInput


def processRequest(rawInput, relationships):

    # Define output values
    relationship = None
    personX = None
    personY = None
    result = None

    # Process the raw input into a easy to use dictionary
    processedInput = processInput(rawInput)

    # Update the output values
    relationship = processedInput["relationship"]
    personX = processedInput["x"]
    personY = processedInput["y"]

    # Verify that the request has usable values
    verifiedInput = verifyInput(processedInput, relationships)

    # Get the result if the request had possible values
    if(verifiedInput):
        result = relationships.dispatchFunction[relationship](personX, personY)

    # Return the results as a dictionary because tuples cause troubles
    return {"relationship": relationship, "x": personX, "y": personY, "result": result}


def main():
    relationships = Relationships()
    makeRelationshipOutput(relationships, "RelationshipOutput.csv")

    print("\nStrict Request Format: 'RELATIONSHIP PERSON_X PERSON_Y'")
    print("Easy Request Format: '[is/Is] PERSON_Y PERSON_X['s] RELATIONSHIP[?]'")
    print("Type 'exit' to quit")

    while(True):
        # Get request as raw input
        print("\nWhat relationship would you like to know about?")
        rawInput = input()

        # Safe exit for the program
        if(rawInput.strip().lower().startswith("exit")):
            break

        # Process the request
        request = processRequest(rawInput, relationships)

        # If the request lead to a result, print it, otherwise, inform that it wasn't a good request
        if(request["result"] != None):
            print(
                f"({request['result']}) {request['y']} is {'NOT ' if not request['result'] else ''}{request['x']}'s {request['relationship']}.")
        else:
            print("That request could not be processed.")


main()
