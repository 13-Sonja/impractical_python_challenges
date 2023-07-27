"""Generate funny names."""

import sys
import random
from pyfiglet import Figlet

first = (
    "Bill",
    "Bob",
    "Boxelder",
    "Bud",
    "Chad",
    "Chesterfield",
    "Chigger",
    "Cinnabuns",
    "Cleet",
    "Cornbread",
    "Crab Meat",
    "Crapps",
    "Dark Skies",
    "Dennis",
    "Dicman",
    "Elphonso",
    "Figgs",
    "Foncy",
    "Gootsy",
    "Greasy Jim",
    "Huckleberry",
    "Huggy",
    "Ignatious",
    "Jim",
    "Jimbo",
    "Jefferson",
    "Jenkins",
    "Joe",
    "Johnny",
    "Longbranch",
    "Mary",
    "Mergatroid",
    "Mr Peabody",
    "Ovaltine",
    "Pennywhistle",
    "Pitchfork Ben",
    "Schlomo",
    "Scratchensniff",
    "Scut",
    "Sid",
    "Skidmark",
    "Slaps",
    "Snakes",
    "Snoobs",
    "Snorki",
    "Soupcan Sam",
    "Squids",
    "Steve",
    "Storyboard",
    "Sweet Tea",
    "TeeTee",
    "Wheezy",
    "Winston",
    "Porkins",
    "Putney",
    "Worms",
    "Boaty",
)

middle = (
    "Baby Oil",
    "Bad News",
    "Beenie-Weenie",
    "Big Burps",
    "Bowel Noises",
    "Butterbean",
    "Buttermilk",
    "Buttocks",
    "Chewy",
    "Clawhammer",
    "Fancypants",
    "Jazz Hands",
    "Lemongrass",
    "Lil Debil",
    "Lunch Money",
    "Oil-Can",
    "Oinks",
    "Old Scratch",
    "Potato Bug",
    "Pushmeet",
    "Pottin Soil",
    "Rock Candy",
    "Stinkbug",
    "Stinky",
    "The Squirts",
)

last = (
    "Appleyard",
    "Bigmeat",
    "Bloominshine",
    "Boogerbottom",
    "Breedslovetrout",
    "Butterbaugh",
    "Clovenhoof",
    "Clutterbuck",
    "Cocktoasten",
    "Endicott",
    "Fewhairs",
    "Gooberdapple",
    "Goodensmith",
    "Goodpasture",
    "Guster",
    "Henderson",
    "Hooperbag",
    "Hoosenater",
    "Hootkins",
    "Jefferson",
    "Jenkins",
    "Jingley-Schmidt",
    "Johnson",
    "Kingfish",
    "Listenbee",
    "M'Bembo",
    "McBoatface",
    "McFadden",
    "Moonshine",
    "Nettles",
    "Noseworthy",
    "Olivetti",
    "Outerbridge",
    "Overpeck",
    "Overturf",
    "Oxhandler",
    "Pealike",
    "Pennywhistle",
    "Peterson",
    "Pieplow",
    "Pinkerton",
    "Quakenbush",
    "Rainwater",
    "Rosenthal",
    "Rubbins",
    "Sackrider",
    "Snuggleshine",
    "Splern",
    "Stevens",
    "Stroganoff",
    "Sugar-Gold",
    "Swackhamer",
    "Tippins",
    "Turnipseed",
    "Vinaigrette",
    "Walkingstick",
    "Wallbanger",
    "Weewax",
    "Weiners",
    "Whipkey",
    "Wigglesworth",
    "Wimplesnatch",
    "Winterkorn",
    "Woolysocks",
)


def main():
    """Generates random names including middle names from three lists until the user stops the app."""
    figlet = Figlet()
    figlet.setFont(font="cybermedium")
    print("Welcome to the pseudonym generator!")
    print("\nYour first pseudonym is:")
    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        middle_variable = random.choice((1, 2, 3))
        if middle_variable == 1:
            middle_name = random.choice(middle)
            text = f"{first_name} {middle_name} {last_name}"
            print(figlet.renderText(text))
        else:
            text = f"{first_name} {last_name}"
            print(figlet.renderText(text))

        choice = input("Press Enter to try again or 'q' to quit:  ").lower()
        if choice == "q":
            sys.exit("Goodbye!")


if __name__ == "__main__":
    main()
