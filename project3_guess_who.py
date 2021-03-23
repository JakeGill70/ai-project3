from KnowledgeBase import KnowledgeBase


def printPopositionialLogic():
    '''
        Helper method used to generate the propositional logic necessary
        for project 3 part 1.

        Unless intentially modified, this code is not used in the main method.
    '''
    print("Propositional Logic: ")
    for c in kb.characters:
        s += f"{c['Name']}: NAME_{c['Name']}_ = \"{c['Name']}\" ꓥ "
        s += f"{c['Gender']} ꓥ {c['Hair Color']}Hair_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Bald']=='False' else ''}Bald_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Hat']=='False' else ''}Hat_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Mustache']=='False' else ''}Mustache_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Beard']=='False' else ''}Beard_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Glasses']=='False' else ''}Glasses_{c['Name']}_ ꓥ "
        s += f"{'¬' if c['Earrings']=='False' else ''}Earrings_{c['Name']}_"
        print(s)


def main():
    """
        Driver Method
    """
    kb = KnowledgeBase()

    # printPopositionialLogic()

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

        print(f"Asking about {bc[0]} being {bc[1]}...")
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
