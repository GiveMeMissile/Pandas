Key = 0
import pandas as I_Imprison_Pandas
dict = { "Character": ["Power", "Morals", "Entertainment", "Enemy", "Favorite food", "Relationships", "Occupation"], "(Example) Blaze": ["Fire", "Very Evil", "Burning people alive for her own entertainment", "Anything that moves", "Burnt Steak", "None","Burning things"]}
Example = I_Imprison_Pandas.DataFrame(dict)
print(Example)
print("This is an example of a character list. You can create your own character by filling up this list.")
while Key < 1:
    Char = input("What do you want your character's name to be?: ")
    Pow = input("What do you want your character's power to be?: ")
    Mor = input("What moral orientation do you want your character to have?: ")
    Ent = input("What dose your character do to entertain themselves?: ")
    Ene = input("Who is your character's enemy if they have one?: ")
    Faf = input("What is your character's favorite food? ")
    Rel = input("What type of relationships dose your character have to other characters/people?: ")
    dict = {"Character": ["Power", "Morals", "Specialty", "Enemy", "Favorite food", "Relationships"], Char: [Pow, Mor, Ent, Ene, Faf, Rel]}
    Character = I_Imprison_Pandas.DataFrame(dict)
    print(Character)
    Continue = input("Do you want to make another character list?(yes or no): ")
    if(Continue == "yes"):
        print("Ok lets Continue")
    else:
        print("Thank you for making lists. Have a nice day (:")
        Key += 100000000000
