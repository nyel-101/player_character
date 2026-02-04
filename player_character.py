class PlayerCharacter:
    def __init__(self, playerName):
        self.playerName = playerName        # Public attribute
        self.__healthPoints = 100           # Private attribute

    def takeDamage(self, amount):
        if amount > 0:
            self.__healthPoints -= amount
            if self.__healthPoints < 0:
                self.__healthPoints = 0
            print(f"{self.playerName} took {amount} damage.")
        else:
            print("Invalid damage amount.")

    def heal(self, amount):
        if amount > 0:
            self.__healthPoints += amount
            print(f"{self.playerName} healed by {amount}.")
        else:
            print("Invalid healing amount.")

    def get_status(self):
        print(f"Player: {self.playerName}")
        print(f"Health Points: {self.__healthPoints}")

    def updateName(self, new_name):
        self.playerName = new_name
        print(f"Player name updated to '{new_name}'.")

    def _gm_setHP(self, new_hp, gm_code):
        if gm_code == "GM123":
            self.__healthPoints = new_hp
            print(f"Game Master set HP of {self.playerName} to {new_hp}.")
        else:
            print("Invalid Game Master code. Access denied.")

# Character database
characters = {
    "Hero1": PlayerCharacter("Nullroot")
}

# Main menu loop
while True:
    print("\nPLAYER CHARACTER SYSTEM")
    print("1. Create Multiple Characters")
    print("2. View All Characters")
    print("3. Take Damage")
    print("4. Heal Character")
    print("5. Game Master Override HP")
    print("6. Update Character Name")
    print("7. Delete Character")
    print("8. Encapsulation Test")
    print("9. Exit")

    choice = input("Choose an option (1-9): ").strip()

    if choice == "1":
        count = int(input("How many characters do you want to create? "))
        for i in range(count):
            print(f"\nCreating character {i+1} of {count}")
            key = input("Enter character ID: ")
            if key in characters:
                print("Character ID already exists.")
            else:
                name = input("Enter player name: ")
                characters[key] = PlayerCharacter(name)
                print(f"Character '{key}' created.")

    elif choice == "2":
        print("\nAll Characters:")
        if not characters:
            print("No characters available.")
        else:
            for key, char in characters.items():
                print(f"\nCharacter ID: {key}")
                char.get_status()

    elif choice == "3":
        key = input("Enter character ID to damage: ")
        if key in characters:
            amount = int(input("Enter damage amount: "))
            characters[key].takeDamage(amount)
        else:
            print("Character not found.")

    elif choice == "4":
        key = input("Enter character ID to heal: ")
        if key in characters:
            amount = int(input("Enter healing amount: "))
            characters[key].heal(amount)
        else:
            print("Character not found.")

    elif choice == "5":
        key = input("Enter character ID for GM override: ")
        if key in characters:
            new_hp = int(input("Enter new HP value: "))
            gm_code = input("Enter Game Master code: ")
            characters[key]._gm_setHP(new_hp, gm_code)
        else:
            print("Character not found.")

    elif choice == "6":
        key = input("Enter character ID to rename: ")
        if key in characters:
            new_name = input("Enter new player name: ")
            characters[key].updateName(new_name)
        else:
            print("Character not found.")

    elif choice == "7":
        key = input("Enter character ID to delete: ")
        if key in characters:
            del characters[key]
            print(f"Character '{key}' deleted.")
        else:
            print("Character not found.")

    elif choice == "8":
        print("\nEncapsulation Test:")
        for key, char in characters.items():
            print(f"\nCharacter ID: {key}")
            try:
                char.__healthPoints = 9999
                print("Direct modification attempted.")
            except:
                print("Direct modification blocked.")
            char.get_status()

        
        print("Exiting character system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 9.")