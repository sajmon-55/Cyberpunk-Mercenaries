class Entity:
    def __init__(self, name: str, hp: int, strength: int, reflex: int, iq: int):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.reflex = reflex
        self.iq = iq

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

        super().__init__(
            name=name,
            hp=stats["hp"],
            strength=stats["strength"],
            reflex=stats["reflex"],
            iq=stats["iq"]
        )

        self.origin = origin
        self.lv = 1
        self.exp = 0
        self.cash = 500

        self.reputation = {
            "City Center": 0.0,
            "Watson": 0.0,
            "Westbrook": 0.0,
            "Heywood": 0.0,
            "Santo Domingo": 0.0,
            "Pacifica": 0.0,
            "Badlands": 0.0,
            "Dogtown": 0.0,
        }

        self.inventory = []
        self.equipped_weapon = None
        self.hacks = []
        self.cyberware = []
        self.cyberpsychosis = 0
        # Nie wiem ile
        self.max_cyberpsychosis = None
