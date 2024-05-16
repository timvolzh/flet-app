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
                 acrobatics={
                     "baseStat": "dex",
                     "name": "acrobatics",
                     "label": "Акробатика"
                 },
                 investigation={
                     "baseStat": "int",
                     "name": "investigation",
                     "label": "Анализ"
                 },
                 athletics={
                     "baseStat": "str",
                     "name": "athletics",
                     "label": "Атлетика"
                 },
                 perception={
                     "baseStat": "wis",
                     "name": "perception",
                     "label": "Восприятие"
                 },
                 survival={
                     "baseStat": "wis",
                     "name": "survival",
                     "label": "Выживание"
                 },
                 performance={
                     "baseStat": "cha",
                     "name": "performance",
                     "label": "Выступление"
                 },
                 intimidation={
                     "baseStat": "cha",
                     "name": "intimidation",
                     "label": "Запугивание"
                 },
                 history={
                     "baseStat": "int",
                     "name": "history",
                     "label": "История"
                 },
                 sleight_of_hand={
                     "baseStat": "dex",
                     "name": "sleight of hand",
                     "label": "Ловкость рук"
                 },
                 arcana={
                     "baseStat": "int",
                     "name": "arcana",
                     "label": "Магия",
                     "isProf": 1
                 },
                 medicine={
                     "baseStat": "wis",
                     "name": "medicine",
                     "label": "Медицина",
                     "isProf": 1
                 },
                 deception={
                     "baseStat": "cha",
                     "name": "deception",
                     "label": "Обман"
                 },
                 nature={
                     "baseStat": "int",
                     "name": "nature",
                     "label": "Природа"
                 },
                 insight={
                     "baseStat": "wis",
                     "name": "insight",
                     "label": "Проницательность",
                     "isProf": 1
                 },
                 religion={
                     "baseStat": "int",
                     "name": "religion",
                     "label": "Религия",
                     "isProf": 1
                 },
                 stealth={
                     "baseStat": "dex",
                     "name": "stealth",
                     "label": "Скрытность"
                 },
                 persuasion={
                     "baseStat": "cha",
                     "name": "persuasion",
                     "label": "Убеждение"
                 },
                 animal_handling={
                     "baseStat": "wis",
                     "name": "animal handling",
                     "label": "Уход за животными"
                 }
                 ):
        # ------
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        # ------
        self.prof_strength = prof_strength
        self.prof_constitution = prof_constitution
        self.prof_dexterity = prof_dexterity
        self.prof_intelligence = prof_intelligence
        self.prof_wisdom = prof_wisdom
        self.prof_charisma = prof_charisma

        # Calculated
        self.PASSIVE_WISDOM = 10 + self.wisdom
        self.INITIATIVE = 0 + (self.dexterity - 10) / 2
        self.PROFICIENCY_BONUS = ''
