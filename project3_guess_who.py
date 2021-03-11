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


main()
