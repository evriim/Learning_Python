"""Generates a sidekick name using random selections from predefined lists."""
import random
import sys

def main():

    """2 random names are selected from the tuples and printed on the screen."""

    print("Welcome to the Sidekick name generator! /n")

    first_name = ("Wifi Wasters", "The Typo Troupe Keyboard Warriors",
    "Roast Post", "Bitmoji Maniacs",
    "Laughter Lounge Hashtag Hustlers", "Pun Intended Virtual Reality",
    "Tickle Tent", "Smile Station",
    "Witty Snappers Binge Buddies Gag Gang",
    "Quirk Quenchers", "The Prank Bank",
    "Chuckle Champs", "Wise Crack Wizards", 
    "LOL Lords", "Emoji Overload",
    "Savage Senders", "Funky Monkeys",
    "Giggle Buffs", "Punchline Pros",
    "Jolly Jesters", "Emoji Analysts Spoof Troop",
    "Wisecrack Warehouse Pun Pundits", "Guffaw Ground",
    "BlabbermouthsSnicker Seekers")

    second_name = ("Amber", "Al", "Anna", "Barb",
    "Barry", "Bea", "Ben", "Brock", "Candice",
    "Cara", "Carrie", "Chris", "Cliff", "Colleen", "Cole",
    "Colin", "Chip", "Daisy", "Drew", "Dee", "Earl", "Ella",
    "Hazel", "Hal", "Ima", "Lou", "Paige",
    )

    while True:
        first = random.choice(first_name)
        second = random.choice(second_name)
        print("Your name is: " + first +" "+ second, file=sys.stderr)
        j = input("Do you like it? /n 'Y' for yes, 'N' no... ").lower()
        if j == "y":
            break

    print("Good bye!")

if __name__ == "__main__":
    main()
