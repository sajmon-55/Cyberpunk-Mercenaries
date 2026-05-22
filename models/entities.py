class Entity:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)


class Player(Entity):
    def __init__(self, name: str, origin: str):

        starting_stats = {
            "Korpo": {"hp": 120, "strength": 4, "reflex": 4, "iq": 8},
            "Street kid": {"hp": 120, "strength": 4, "reflex": 8, "iq": 4},
            "Nomad": {"hp": 120, "strength": 8, "reflex": 4, "iq": 4},
        }

        stats = starting_stats.get(origin)

        # Teraz do klasy bazowej przekazujemy TYLKO imię i HP
        super().__init__(name=name, hp=stats["hp"])

        # Statystyki bojowe przypisujemy bezpośrednio do Gracza
        self.strength = stats["strength"]
        self.reflex = stats["reflex"]
        self.iq = stats["iq"]

        self.origin = origin
        self.lv = 1
        self.exp = 0
        self.cash = 500

        self.reputation = {
            "City Center": 0.0, "Watson": 0.0, "Westbrook": 0.0, "Heywood": 0.0,
            "Santo Domingo": 0.0, "Pacifica": 0.0, "Badlands": 0.0, "Dogtown": 0.0,
        }

        self.inventory = []
        self.equipped_weapon = None
        self.hacks = []
        self.cyberware = []
        self.cyberpsychosis = 0
        # nie wiem ile
        self.max_cyberpsychosis = None


class Enemy(Entity):
    def __init__(self, name: str, hp: int, faction: str, base_dmg: int, exp_reward: int, cash_reward: int):
        super().__init__(name=name, hp=hp)

        # iq reflex strength
        faction_types = {
            "Maelstrom": {"weakness": "iq", "advantage": "reflex"},  # Watson
            "Voodoo Boys": {"weakness": "strength", "advantage": "iq"},  # Pacifica
            "Animals": {"weakness": "reflex", "advantage": "strength"},  # Pacifica
            "Arasaka": {"weakness": None, "advantage": "iq"},  # City Center
            "Militech": {"weakness": None, "advantage": "strength"},  # City Center
            "Barghest": {"weakness": None, "advantage": "reflex"},  # Dogtown
            "Tyger Claws": {"weakness": "reflex", "advantage": None},  # Westbrook / Watson
            "Valentinos": {"weakness": None, "advantage": None},  # Heywood
            "6th Street": {"weakness": "reflex", "advantage": None},  # Santo Domingo
            "Wraiths": {"weakness": "reflex", "advantage": "strength"}  # Badlands
        }

        # Pobieramy słabości i przewagi dla podanej frakcji (zabezpieczone na wypadek braku frakcji)
        faction_data = faction_types.get(faction, {"weakness": None, "advantage": None})

        self.faction = faction
        self.weakness = faction_data["weakness"]
        self.advantage = faction_data["advantage"]
        self.base_dmg = base_dmg
        self.exp_reward = exp_reward
        self.cash_reward = cash_reward