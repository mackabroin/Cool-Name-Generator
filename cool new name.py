import random

animal = ["Tiger", "Lion", "Horse", "Shark", "Badger", "Crocodile", "Gorilla", "Tyrannosaurus Rex", "Orca", "Weasel",
          "Velociraptor", "Hawk", "Giraffe", "Cheetah", "Polar Bear", "Grizzly Bear", "Bighorn Ram", "Mantis",
          "Giant Squid", "Sperm Whale", "Komodo Dragon", "Box Jellyfish", "Alligator", "Leopard Seal", "Hyena", "Hippo",
          "Stingray", "Bald Eagle", "Anaconda", "Leopard", "Cobra"]

attribute = ["Courageous", "Stouthearted", "Fragrant", "Vivacious", "Ruthless", "Unstoppable", "Disarming", "Valiant",
             "Noble", "Cunning", "Heroic", "Unstoppable", "Dastardly", "Bold", "Fearsome", "Fierce", "Bloodthirsty",
             "Serene", "Majestic", "Rakish", "Notorious", "Enigmatic", "Magnetic", "Charismatic"]

color = ["Azure", "Blue", "Cyan", "Crimson", "Red", "Scarlet", "Beige", "Taupe", "Mahogany", "Pink", "Violet", "Indigo",
         "Turquoise", "Aquamarine", "Hunter Green", "Green", "Gray", "Black", "Yellow", "Golden", "Silver", "Sienna",
         "Lilac", "Pewter", "Orange", "Magenta", "Yellow", "Mint Green", "Orange", "Marigold"]


def realCoolname():
    print(random.choice(attribute), random.choice(color), random.choice(animal))


while True:

    user_name = input("Give your name and I will transform it. Type done when you are done.")

    done = user_name.lower().strip() == 'done'

    steveAlert = user_name.lower().strip() == 'steve'

    if steveAlert:
        print("Swampy Warty Penisfarter")
        break

    if done:
        print("Later, gator.")
        break

    realCoolname()

print(realCoolname)
