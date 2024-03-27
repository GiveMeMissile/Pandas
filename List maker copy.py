import pandas as Why_a_panda
def names():
    name = input("What is your name?: ")
    return name
def questions():
    Name = names()
    Food = input("What is your favorite food?: ")
    Animal = input("What is your favorite animal: ")
    Subject = input("What is your favorite subject?: ")
    Movie = input("What is your favorite movie?: ")
    Doomsday = input("What is your favorite way humanity could go extinct?: ")
    dict = { "Name": ["Food", "Animal", "Subject", "Movie", "Extinction Event"], Name: [Food, Animal, Subject, Movie, Doomsday] }
    List = Why_a_panda.DataFrame(dict)
    return List
def results():
    Name = names()
    List = questions()
    print(List)
    ask = input("Do you like your list?: ")
    if(ask == "no"):
        print("Well you made it so that is kind of your fault %s." % (Name))
    else:
        if(ask == "yes"):
            print("Noice. Thank you for your time and have a good day %s." % (Name))
        else:
            print("Ok?")
results()
