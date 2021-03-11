import csv
import random

class KnowledgeBase:

    def __init__(self):
        """
            Initialization of the KnowledgeBase class, with the following attributes:

            self.characters - A list of character dictionaries
            self.characteristics - The master list of characteristics and values for all characters
                                    This dictionary should be used to track characteristics to help
                                    in solving the problem.
            self.the_character - The random character to interrogate
        """
        self.characters = []            # A list of all characters, initially (which are dictionaries)
        self.characteristics = {}       # A dictionary of all known characteristics

        # -- Read the characters and characteristics
        self.read_characters()

        # Get a random character to interrogate
        self.the_character = random.choice(self.characters)

    def read_characters(self):
        """
            Sets up the Character Dictionaries and adds them to the characters list.
            Reads from CSV file characters.csv
        """
        with open('characters.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for character in reader:
                self.characters.append(character)


    def tell(self,key,value):
    def tell(self, key, value):
        """
            Tell the KnowledgeBase a new piece of information.
        """
        # Track this characteristic
        self.characteristics[key] = value
        # Remove characters that do not meet this requirement
        self.characters = self.ask_vars(key, value)

    def ask(self, key, value):
        """
            Queries the_character about a specific key, value pair
        """
        hasCharacteristic = (self.the_character[key] == value)
        isBooleanValue = (value == "True" or value == "False")

        if(isBooleanValue):
            return str(hasCharacteristic)
        else:
            if(not hasCharacteristic):
                value = "not " + value
            return value

    def ask_vars(self,key,value):
        """
            Returns the list of remaining characters that meet the key,value pair
        """
        raise NotImplementedError()
        return []
