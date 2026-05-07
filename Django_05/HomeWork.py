class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.take_damage(self.attack_power)
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def show_info(self):
        print(str(self))

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, здоровье {self.health}, атака {self.attack_power}"

    def __add__(self, other):
        return [self, other]

    def __lt__(self, other):
        return self.attack_power < other.attack_power

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.health == other.health
            and self.attack_power == other.attack_power
        )

    def __len__(self):
        return self.health

    def __bool__(self):
        return self.health > 0


class Warrior(Character):
    def attack(self, other):
        damage = self.attack_power + 5
        other.take_damage(damage)
        print(f"Воин {self.name} бьёт мечом {other.name} и наносит {damage} урона.")


class Mage(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, other):
        if self.mana >= 10:
            damage = self.attack_power + 10
            self.mana -= 10
            other.take_damage(damage)
            print(f"Маг {self.name} использует заклинание против {other.name} и наносит {damage} урона.")
        else:
            super().attack(other)


class Archer(Character):
    def attack(self, other):
        damage = self.attack_power + 2
        other.take_damage(damage)
        print(f"Лучник {self.name} стреляет в {other.name} и наносит {damage} урона.")


warrior = Warrior("Артур", 120, 20)
mage = Mage("Мерлин", 80, 18, 30)
archer = Archer("Робин", 90, 16)

characters = [warrior, mage, archer]

for character in characters:
    character.show_info()

print(warrior < mage)
print(warrior == Warrior("Артур", 120, 20))
print(len(archer))
print(bool(mage))
print(warrior + archer)

warrior.attack(mage)
mage.attack(archer)
archer.attack(warrior)

print(bool(mage))
