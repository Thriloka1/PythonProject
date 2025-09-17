# color=input("enter a color: ")
# plural_noun=input("enter a plural noun: ")
# celebrity=input("enter a celebrity: ")
#
#
# print(f"roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"i love {celebrity}")


import random

def play_mad_libs():
    # Different story templates with placeholders
    stories = [
        "One day, {name} went to {place}. There they saw a {adjective} {animal} that wanted to {verb}. They shared some {food} and became best friends!",
        "In the land of {place}, {name} was on a quest to find a {adjective} {animal}. But first, they had to {verb} across a river made of {food}.",
        "{name} always dreamed of visiting {place}. But when they arrived, a {adjective} {animal} asked them to {verb} before they could eat {food} together."
    ]

    print("\n🎉 Welcome to Mad Libs! 🎉")
    print("Fill in the blanks to create a silly story.\n")

    # Ask for user input
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a food: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb (present tense): ")

    # Pick a random story and fill it with user input
    story_template = random.choice(stories)
    story = story_template.format(
        name=name, place=place, animal=animal, food=food, adjective=adjective, verb=verb
    )

    print("\n📖 Here is your Mad Libs story:\n")
    print(story)

# Main game loop
while True:
    play_mad_libs()
    again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("\nThanks for playing! Goodbye! 👋")
        break
