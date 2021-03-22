import csv
import random
import sys


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

    def get_most_impactful_characteristic(self):
        """
            Look through each of the possible variable characteristics
            to determine which answer would remove the most suspects
            from the self.characters list.
            Returms a tuple (Name, Value, # of remaining characters if true)
        """
        # Determine what characteristics have multiple choices
        possibleCharacteristics = self.get_variable_characteristics()

        bestCharacteristic = ""
        bestValue = ""
        bestLen = 999999999

        for key, values in possibleCharacteristics.items():
            # Ignore the name, because if names are unique, then guessing a name
            # would always elimate the most remaining characters.
            if(key == "Name"):
                continue
            for value in values:
                # Count the number of remaining suspects if the answer to the question is true
                currLen = len(self.ask_vars(key, value))
                # If the number of remaining suspects lower than anything else found so far,
                # then store the question that asks about that characteristic and gives that result.
                if(currLen < bestLen):
                    bestLen = currLen
                    bestCharacteristic = key
                    bestValue = value

        # If no other characteristic could trim down the number of remaining characters,
        # Then consider the name as the best characteristic.
        # Considering that any name would elimate all other suspects if guessed correctly,
        # no name is a better guess than any other. With that in mind, the first name
        # available is used to simplicity of implmementation.
        if(bestCharacteristic == ""):
            bestCharacteristic = "Name"
            bestValue = possibleCharacteristics["Name"][0]

        return (bestCharacteristic, bestValue, bestLen)

    def get_variable_characteristics(self):
        """
            Returns a dictionary of characteristics that have more than
            one possible value from the remaining population of 
            characters. The key is the name of the characteristic.
            The value is a list of all possible values that the
            characteristic could be from the remaining characters.
        """

        # Initialize the attributes dictionary with each
        # characteristic being an empty list of possible values
        possible_Characteristics = {}
        for key, value in self.characters[0].items():
            possible_Characteristics[key] = []

        # Go through each remaining character and add their
        # value to the list of possible values if the list
        # does not already contain that value
        for char in self.characters:
            for key, value in char.items():
                if(value not in possible_Characteristics[key]):
                    possible_Characteristics[key].append(value)

        # Determine what characteristics only have one
        # possible value
        keysToDelete = []
        for key, values in possible_Characteristics.items():
            if(len(values) == 1):
                keysToDelete.append(key)

        # Remove all characteristics that only have one
        # possible value, because it offers no possibility
        # for what that characteristic could be, only
        # a certainity of what it is.
        for key in keysToDelete:
            del possible_Characteristics[key]

        return possible_Characteristics

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
        # Determine if the secret character has the specific characteristic value
        hasCharacteristic = (self.the_character[key] == value)
        # Determine if that characteristic is a boolean choice
        isBooleanValue = (value == "True" or value == "False")

        # If the characteristic is boolean, just return it as a string
        if(isBooleanValue):
            return str(hasCharacteristic)
        else:
            # If the characteristic is NOT boolean...
            # Return the value if the secret character has the characteristic,
            # and prepend "not " if the secret character does not have the characteristic.
            if(not hasCharacteristic):
                value = "not " + value
            return value

    def ask_vars(self, key, value):
        """
            Returns the list of remaining characters that meet the key,value pair
        """
        possibleChars = []

        # This function needs to check for characters that do not have
        # the given value for the given characteristic (key) if the value
        # starts with a "not ".
        isNegated = value.startswith("not ")

        # If a "not " was prepended to indicate negation, then the "not "
        # needs to be removed from the value so that comparisons can be
        # performed on the value.
        if(isNegated):
            value = value[4:]

        # Loops through every remaining character to see who meets the constraint
        # defined by the key value pair.
        for character in self.characters:
            charValue = character[key]
            # Determine if the character has the value
            hasValue = (charValue == value)
            # Determine if the character should have the value (considering negation)
            # This looks odd, but it is just how python handles XOR
            shouldAppend = (hasValue != isNegated)
            # Append the character to the list of remaining characters that the
            # secret character could be if the character meets the above
            # characteristic criteria.
            if(shouldAppend):
                possibleChars.append(character)

        return possibleChars
