from typing import Dict, List, Optional


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: Optional[List[Dict]], weapon: Dict,
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


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    """Simulates battles between knights based on their configurations.

    Args:
        knights_config: A dictionary containing knight configurations (name, power, hp, etc.).

    Returns:
        A dictionary with the remaining HP of each knight after the battles.
    """

    # Prepare knights for battle (moved logic from main)
    knights = {}
    for name, config in knights_config.items():
        knights[name] = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config["weapon"],
            potion=config.get("potion"),
        )

    # Simulate battles
    results = {}
    for attacker_name, defender_name in [("Lancelot", "Mordred"), ("Arthur", "Red Knight")]:
        attacker = knights[attacker_name]
        defender = knights[defender_name]
        damage_dealt = max(0, attacker.power - defender.protection)
        attacker.receive_damage(damage_dealt)
        defender.receive_damage(damage_dealt)
        results[attacker_name] = attacker.hp
        results[defender_name] = defender.hp

    return results


def main():
    knights = {
        "lancelot": {
            "name": "Lancelot",
            "power": 35,
            "hp": 100,
            "armour": [],
            "weapon": {
                "name": "Metal Sword",
                "power": 50,
            },
            "potion": None,
        },
        "arthur": {
            "name": "Arthur",
            "power": 45,
            "hp": 75,
            "armour": [
                {
                    "part": "helmet",
                    "protection": 15,
                },
                {
                    "part": "breastplate",
                    "protection": 20,
                },
                {
                    "part": "boots",
                    "protection": 10,
                }
            ],
            "weapon": {
                "name": "Two-handed Sword",
                "power": 55,
            },
            "potion": None,
        },
        "mordred": {
            "name": "Mordred",
            "power": 30,
            "hp": 90,
            "armour": [
                {
                    "part": "breastplate",
                    "protection": 15,
                },
                {
                    "part": "boots",
                    "protection": 10,
                }
            ],
            "weapon": {
                "name": "Poisoned Sword",
                "power": 60,
            },
            "potion": {
                "name": "Berserk",
                "effect": {
                    "power": +15,
                    "hp": -5,
                    "protection": +10,
                }
            }
        },
        "red_knight": {
            "name": "Red Knight",
            "power": 40,
            "hp": 70,
            "armour": [
                {
                    "part": "breastplate",
                    "protection": 25,
                }
            ],
            "weapon": {
                "name": "Sword",
                "power": 45
            },
            "potion": {
                "name": "Blessing",
                "effect": {
                    "hp": +10,
                    "power": +5,
                }
            }
        }
    }

    def battles(knightsConfig):
        # BATTLE PREPARATIONS:

        # lancelot
        lancelot = knightsConfig["lancelot"]

        # apply armour
        lancelot["protection"] = 0
        for a in lancelot["armour"]:
            lancelot["protection"] += a["protection"]

        # apply weapon
        lancelot["power"] += lancelot["weapon"]["power"]

        # apply potion if exist
        if lancelot["potion"] is not None:
            if "power" in lancelot["potion"]["effect"]:
                lancelot["power"] += lancelot["potion"]["effect"]["power"]

            if "protection" in lancelot["potion"]["effect"]:
                lancelot["protection"] += lancelot["potion"]["effect"]["protection"]

            if "hp" in lancelot["potion"]["effect"]:
                lancelot["hp"] += lancelot["potion"]["effect"]["hp"]

        # arthur
        arthur = knightsConfig["arthur"]

        # apply armour
        arthur["protection"] = 0
        for a in arthur["armour"]:
            arthur["protection"] += a["protection"]

        # apply weapon
        arthur["power"] += arthur["weapon"]["power"]

        # apply potion if exist
        if arthur["potion"] is not None:
            if "power" in arthur["potion"]["effect"]:
                arthur["power"] += arthur["potion"]["effect"]["power"]

            if "protection" in arthur["potion"]["effect"]:
                arthur["protection"] += arthur["potion"]["effect"]["protection"]

            if "hp" in arthur["potion"]["effect"]:
                arthur["hp"] += arthur["potion"]["effect"]["hp"]

        # mordred
        mordred = knightsConfig["mordred"]

        # apply armour
        mordred["protection"] = 0
        for a in mordred["armour"]:
            mordred["protection"] += a["protection"]

        # apply weapon
        mordred["power"] += mordred["weapon"]["power"]

        # apply potion if exist
        if mordred["potion"] is not None:
            if "power" in mordred["potion"]["effect"]:
                mordred["power"] += mordred["potion"]["effect"]["power"]

            if "protection" in mordred["potion"]["effect"]:
                mordred["protection"] += mordred["potion"]["effect"]["protection"]

            if "hp" in mordred["potion"]["effect"]:
                mordred["hp"] += mordred["potion"]["effect"]["hp"]

        # red_knight
        red_knight = knightsConfig["red_knight"]

        # apply armour
        red_knight["protection"] = 0
        for a in red_knight["armour"]:
            red_knight["protection"] += a["protection"]

        # apply weapon
        red_knight["power"] += red_knight["weapon"]["power"]

        # apply potion if exist
        if red_knight["potion"] is not None:
            if "power" in red_knight["potion"]["effect"]:
                red_knight["power"] += red_knight["potion"]["effect"]["power"]

            if "protection" in red_knight["potion"]["effect"]:
                red_knight["protection"] += red_knight["potion"]["effect"]["protection"]

            if "hp" in red_knight["potion"]["effect"]:
                red_knight["hp"] += red_knight["potion"]["effect"]["hp"]

        # -------------------------------------------------------------------------------
        # BATTLE:

        # 1 Lancelot vs Mordred:
        lancelot["hp"] -= mordred["power"] - lancelot["protection"]
        mordred["hp"] -= lancelot["power"] - mordred["protection"]

        # check if someone fell in battle
        if lancelot["hp"] <= 0:
            lancelot["hp"] = 0

        if mordred["hp"] <= 0:
            mordred["hp"] = 0

        # 2 Arthur vs Red Knight:
        arthur["hp"] -= red_knight["power"] - arthur["protection"]
        red_knight["hp"] -= arthur["power"] - red_knight["protection"]

        # check if someone fell in battle
        if arthur["hp"] <= 0:
            arthur["hp"] = 0

        if red_knight["hp"] <= 0:
            red_knight["hp"] = 0

        # Return battle results:
        return {
            lancelot["name"]: lancelot["hp"],
            arthur["name"]: arthur["hp"],
            mordred["name"]: mordred["hp"],
            red_knight["name"]: red_knight["hp"],
        }

    print(battles(knights))
