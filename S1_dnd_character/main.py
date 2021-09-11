import os
import random

races = ["human", "orc", "dwarf", "elf"]
classes = ["barbarian", "druid", "wizard"]
backgrounds = ["acolyte", "charlatan", "criminal", "entertainer",
               "folkhero", "guildartisan", "hermit", "noble",
               "outlander", "sage", "sailor", "soldier", "urchin"]
sexes = ["male", "female"]

# Better way to insert this data is with a csv file
# Read the data in instead of manually creating dictionaries
# which might have errors while copying data.

data = {"human": [-1, 0, 1, 3],
        "elf": [0, 2, 1, 1],
        "orc": [3, 2, -1, -1],
        "dwarf": [2, 0, -2, 2],
        "barbarian": [4, 1, 0, 0],
        "druid": [2, 0, 1, 2],
        "wizard": [0, 0, 0, 4],
        "acolyte": [0, 0, 0, 4],
        "charlatan": [0, 0, 3, 2],
        "criminal": [0, 4, 0, 0],
        "entertainer": [0, 2, 3, 0],
        "folkhero": [3, 0, 2, 0],
        "guildartisan": [0, 0, 0, 5],
        "hermit": [3, 0, 0, 3],
        "noble": [0, 0, 5, 0],
        "outlander": [2, 1, 1, 1],
        "sage": [0, 0, 2, 3],
        "sailor": [0, 3, 2, 0],
        "soldier": [4, 1, 0, 0],
        "urchin": [0, 5, 0, 0]
        }


class NameFileFinder:
    def __init__(self, race, sex):
        self.dir_index = {}
        for i in os.listdir('data'):
            file_name = i.split(".")[0]
            if "_" in file_name:
                self.file_race = file_name.split("_")[0]
                self.file_sex = file_name.split("_")[1]
                self.dir_index[f'{self.file_race}_{self.file_sex}'] = i
            elif "-" in file_name:
                self.file_race = file_name.split("-")[0]
                self.file_sex = file_name.split("-")[1]
                self.dir_index[f'{self.file_race}_{self.file_sex}'] = i
        self.current_file = self.dir_index[f'{race}_{sex}']
        with open(os.path.join('data', self.current_file), 'r') as names_read:
            self.names = names_read.read().splitlines()

    def __repr__(self):
        return random.choice(self.names)


class DnDCharacter:
    def __init__(self, race, dnd_class, bg, sex):
        self.race = race
        self.dnd_class = dnd_class
        self.bg = bg
        self.sex = sex
        self.name = ""
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.charisma = 0
        self.make_strength()
        self.make_dexterity()
        self.make_intelligence()
        self.make_charisma()
        self.make_name()

    def make_name(self):
        self.name = NameFileFinder(self.race, self.sex)
        return self.name

    def make_strength(self):
        self.strength = data[self.race][0] + data[self.dnd_class][0] + data[self.bg][0]
        return self.strength

    def make_dexterity(self):
        self.dexterity = data[self.race][1] + data[self.dnd_class][1] + data[self.bg][1]
        return self.dexterity

    def make_intelligence(self):
        self.intelligence = data[self.race][2] + data[self.dnd_class][2] + data[self.bg][2]
        return self.intelligence

    def make_charisma(self):
        self.charisma = data[self.race][3] + data[self.dnd_class][3] + data[self.bg][3]
        return self.charisma

    def __repr__(self):
        return f'Your Character: \nName: {self.name}\nRace: {self.race.capitalize()}' \
               f'\nClass: {self.dnd_class.capitalize()}\n' \
               f'Background: {self.bg.capitalize()}\n' \
               f'Sex: {self.sex.capitalize()}' \
               f'\nStrength: {self.strength}\nDexterity:{self.dexterity}\n' \
               f'Charisma: {self.charisma}\nIntelligence: {self.intelligence}'


if __name__ == '__main__':
    print("DnD Character Creator")
    available_backgrounds = "Acolyte, Charlatan, Criminal, Entertainer, Folk Hero, " \
                            "Guild Artisan, Hermit, Noble, Outlander, Sage, Sailor, " \
                            "Soldier and Urchin"
    print("\n\n")
    while True:
        try:
            race = input("Enter your character's race[Choices: Human, Orc, Dwarf or Elf]: ").strip().lower()
            assert race in races, "Choices are Human, Orc, Dwarf are Elf"
            break
        except AssertionError:
            print("Choices are Human, Orc, Dwarf are Elf")
            continue
    while True:
        try:
            dnd_class = input("Enter your character's class[Choices: Barbarian, Druid or Wizard]: ").strip().lower()
            assert dnd_class in classes, "Choices are Barbarian, Druid and Wizard"
            break
        except AssertionError:
            print("Choices are Barbarian, Druid and Wizard")
            continue

    print(available_backgrounds)
    while True:
        try:
            background = input("Enter your character's background: ").strip().lower()
            assert background in backgrounds, available_backgrounds
            break
        except AssertionError:
            print(available_backgrounds)
            continue
    while True:
        try:
            sex = input("Enter your character's sex: ").strip().lower()
            assert sex in sexes, "Choices are Male and Female"
            break
        except AssertionError:
            print("Choices are Male and Female")
            continue

    dnd_character = DnDCharacter(race, dnd_class, background, sex)
    print("\n\n")
    print("=" * 10)
    print("\n\n")
    print(dnd_character)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
