from KnowledgeBase import KnowledgeBase


def main():
    """
        Driver Method
    """
    kb = KnowledgeBase()

    print("======================================")
    print(f"Looking for {kb.the_character['Name']}.")
    print(f"{kb.the_character['Name']} looks like this: {kb.the_character}")
    print("The population has the possible set of characteristics: ", kb.get_variable_characteristics())
    print("======================================")
    print("Starting interview... ")
    qCount = 0
    while(True):
        print("======================================")
        qCount += 1
        print(f"Question # {qCount}")
        print("Determing the most impactful characteristic...")
        bc = kb.get_most_impactful_characteristic()
        print(f"The most impactful characteristic is {bc[0]} being {bc[1]}.")

        print("")

        print(f"Asking  about {bc[0]} being {bc[1]}...")
        result = kb.ask(bc[0], bc[1])
        print(f"{bc[0]} being {bc[1]} is {bc[1]==result}.")

        print("")

        print(f"Adding { (bc[0], str(result)) } to my knowledge base...")
        kb.tell(bc[0], str(result))

        print("")

        print(f"Heres what I know: ", kb.characteristics)

        print("")

        possibleCharacteristics = kb.get_variable_characteristics()
        print("The population now only has this set of possible characteristics: ", possibleCharacteristics)

        print("")

        # If there are only unique characteristics left
        if(not possibleCharacteristics):
            print(f"Therefore, the person can only be {kb.characters[0]['Name']}")
            break
        else:
            print("The remaining suspects could be: ", [char['Name'] for char in kb.characters])

        print("")


main()
