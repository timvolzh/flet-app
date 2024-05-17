class Char:
    def __init__(self,

                 # Stats
                 strength: int = 10,
                 constitution: int = 10,
                 dexterity: int = 10,
                 intelligence: int = 10,
                 wisdom: int = 10,
                 charisma: int = 10,

                 # Prof Stats
                 prof_strength: bool = False,
                 prof_constitution: bool = False,
                 prof_dexterity: bool = False,
                 prof_intelligence: bool = False,
                 prof_wisdom: bool = False,
                 prof_charisma: bool = False,

                 # Skills
                 acrobatics={"baseStat": "dex", "name": "acrobatics", "label": "Акробатика"},
                 investigation={"baseStat": "int", "name": "investigation", "label": "Анализ"},
                 athletics={"baseStat": "str", "name": "athletics", "label": "Атлетика"},
                 perception={"baseStat": "wis", "name": "perception", "label": "Восприятие"},
                 survival={"baseStat": "wis", "name": "survival", "label": "Выживание"},
                 performance={"baseStat": "cha", "name": "performance", "label": "Выступление"},
                 intimidation={"baseStat": "cha", "name": "intimidation", "label": "Запугивание"},
                 history={"baseStat": "int", "name": "history", "label": "История"},
                 sleight_of_hand={"baseStat": "dex", "name": "sleight of hand", "label": "Ловкость рук"},
                 arcana={"baseStat": "int", "name": "arcana", "label": "Магия", "isProf": 1},
                 medicine={"baseStat": "wis", "name": "medicine", "label": "Медицина", "isProf": 1},
                 deception={"baseStat": "cha", "name": "deception", "label": "Обман"},
                 nature={"baseStat": "int", "name": "nature", "label": "Природа"},
                 insight={"baseStat": "wis", "name": "insight", "label": "Проницательность", "isProf": 1},
                 religion={"baseStat": "int", "name": "religion", "label": "Религия", "isProf": 1},
                 stealth={"baseStat": "dex", "name": "stealth", "label": "Скрытность"},
                 persuasion={"baseStat": "cha", "name": "persuasion", "label": "Убеждение"},
                 animal_handling={"baseStat": "wis", "name": "animal handling", "label": "Уход за животными"}
                 ):
        # Stats
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        # Prof Bonus
        self.prof_strength = prof_strength
        self.prof_constitution = prof_constitution
        self.prof_dexterity = prof_dexterity
        self.prof_intelligence = prof_intelligence
        self.prof_wisdom = prof_wisdom
        self.prof_charisma = prof_charisma

        # Calculated
        self.PASSIVE_WISDOM = 10 + self.wisdom
        self.INITIATIVE = int(0 + (self.dexterity - 10) / 2)
        self.PROFICIENCY_BONUS = ''

        # Skills
        self.acrobatics = acrobatics
        self.investigation = investigation
        self.athletics = athletics
        self.perception = perception
        self.survival = survival
        self.performance = performance
        self.intimidation = intimidation
        self.history = history
        self.sleight_of_hand = sleight_of_hand
        self.arcana = arcana
        self.medicine = medicine
        self.deception = deception
        self.nature = nature
        self.insight = insight
        self.religion = religion
        self.stealth = stealth
        self.persuasion = persuasion
        self.animal_handling = animal_handling

    def from_dict(self, char=None):
        data = char["data"]

        # Stats
        stats = char["stats"]
        self.strength = int(stats["str"]["score"])
        self.constitution = int(stats["con"]["score"])
        self.dexterity = int(stats["dex"]["score"])
        self.intelligence = int(stats["int"]["score"])
        self.wisdom = int(stats["wis"]["score"])
        self.charisma = int(stats["cha"]["score"])

        # Prof Bonus
        prof = char["saves"]
        self.prof_strength = prof["str"]["isProf"]
        self.prof_constitution = prof["con"]["isProf"]
        self.prof_dexterity = prof["dex"]["isProf"]
        self.prof_intelligence = prof["int"]["isProf"]
        self.prof_wisdom = prof["wis"]["isProf"]
        self.prof_charisma = prof["cha"]["isProf"]

        # Calculated
        self.PASSIVE_WISDOM = 10 + self.wisdom
        self.INITIATIVE = int(0 + (self.dexterity - 10) / 2)
        self.PROFICIENCY_BONUS = ''

        # Skills
        skills = char["skills"]
        self.acrobatics = skills["acrobatics"]
        self.investigation = skills["investigation"]
        self.athletics = skills["athletics"]
        self.perception = skills["perception"]
        self.survival = skills["survival"]
        self.performance = skills["performance"]
        self.intimidation = skills["intimidation"]
        self.history = skills["history"]
        self.sleight_of_hand = skills["sleight_of_hand"]
        self.arcana = skills["arcana"]
        self.medicine = skills["medicine"]
        self.deception = skills["deception"]
        self.nature = skills["nature"]
        self.insight = skills["insight"]
        self.religion = skills["religion"]
        self.stealth = skills["stealth"]
        self.persuasion = skills["persuasion"]
        self.animal_handling = skills["animal_handling"]

        pass

    def to_dict(self, data):
        pass
