from typing import Dict, List, Optional


class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: Optional[List[Dict]], weapon: Dict,
                 potion: Optional[Dict]):
        self.name = name
        self.base_power = power
        self.base_hp = hp
        self.armour = armour or []
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0
        self.hp = 0
        self._calculate_stats()

    def _calculate_stats(self):
        self.protection = sum(a["protection"] for a in self.armour)
        self.power = self.base_power + self.weapon["power"]
        self.hp = self.base_hp
        if self.potion:
            for stat, value in self.potion["effect"].items():
                if stat == "hp":
                    self.hp += value
                elif stat == "power":
                    self.power += value
                elif stat == "protection":
                    self.protection += value

    def receive_damage(self, damage: int):
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0


def simulate_battle(knight1: Knight, knight2: Knight) -> Dict[str, int]:
    damage1 = max(0, knight2.power - knight1.protection)
    damage2 = max(0, knight1.power - knight2.protection)
    knight1.receive_damage(damage1)
    knight2.receive_damage(damage2)
    return {knight1.name: knight1.hp, knight2.name: knight2.hp}


def main():
    KNIGHTS = {
        "lancelot": {
            "name": "Lancelot",
            "power": 35,
            "hp": 100,
            "armour": [],
            "weapon": {"name": "Metal Sword", "power": 50},
            "potion": None,
        },
        "arthur": {
            "name": "Arthur",
            "power": 45,
            "hp": 75,
            "armour": [
                {"part": "helmet", "protection": 15},
                {"part": "breastplate", "protection": 20},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Two-handed Sword", "power": 55},
            "potion": None,
        },
        "mordred": {
            "name": "Mordred",
            "power": 30,
            "hp": 90,
            "armour": [
                {"part": "breastplate", "protection": 15},
                {"part": "boots", "protection": 10},
            ],
            "weapon": {"name": "Poisoned Sword", "power": 60},
            "potion": {"name": "Berserk", "effect": {"power": +15, "hp": -5, "protection": +10}},
        },
        "red_knight": {
            "name": "Red Knight",
            "power": 40,
            "hp": 70,
            "armour": [{"part": "breastplate", "protection": 25}],
            "weapon": {"name": "Sword", "power": 45},
            "potion": {"name": "Blessing", "effect": {"hp": +10, "power": +5}},
        },
    }

    lancelot = Knight(**KNIGHTS["lancelot"])
    mordred = Knight(**KNIGHTS["mordred"])
    arthur = Knight(**KNIGHTS["arthur"])
    red_knight = Knight(**KNIGHTS["red_knight"])

    battle1_result = simulate_battle(lancelot, mordred)
    battle2_result = simulate_battle(arthur, red_knight)

    all_results = {**battle1_result, **battle2_result}
    print(all_results)


if __name__ == "__main__":
    main()
