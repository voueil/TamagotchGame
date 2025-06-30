from random import randrange

class Pet(object):
    ExcitementMinimum = 2
    ExcitementMaximum = 15
    ExcitementWarning = 5

    FoodMinimum = 2
    FoodMaximum = 15
    FoodWarning = 5

    vocab = []

    def __init__(self, name, PetType):
        self.name = name
        self.PetType = PetType
        self.Food = randrange(self.FoodMinimum, self.FoodMaximum)
        self.Excitement = randrange(self.ExcitementMinimum, self.ExcitementMaximum)
        self.vocab = self.vocab[:]  # copy class vocab to instance

    def __clock(self):
        self.Food -= 1
        self.Excitement -= 1

    @property
    def mood(self):
        if self.Food > self.FoodWarning and self.Excitement > self.ExcitementWarning:
            return "happy"
        elif self.Food < self.FoodWarning:
            return "angry"
        else:
            return "bored"

    def __str__(self):
        return "\n i am " + self.name + "\n i feel " + self.mood

    def teach(self, words):
        self.vocab.append(words)
        print("yay! i learned to say:", words)
        self.__clock()

    def talk(self):
        print(" i am a ", self.PetType, " named ", self.name, " i feel ", self.mood)
        if self.vocab:
            print(" i know how to say: ", ", ".join(self.vocab))
        self.__clock()

    def feed(self):
        print("mmm... thank you")
        if self.Food < self.FoodMaximum:
            meal = randrange(1, self.FoodMaximum - self.Food + 1)
            self.Food += meal

        if self.Food < 0:
            self.Food = 0
            print("i am still hungry")
        elif self.Food > self.FoodMaximum:
            self.Food = self.FoodMaximum
            print("i am full")
        self.__clock()

    def play(self):
        if self.Excitement < self.ExcitementMaximum:
            fun = randrange(1, self.ExcitementMaximum - self.Excitement + 1)
            self.Excitement += fun

            if self.Excitement > self.ExcitementMaximum:
                self.Excitement = self.ExcitementMaximum
                print("i am happy")
            elif self.Excitement < 0:
                self.Excitement = 0
                print("i am board")
            else:
                print("yaaay! that was fun")
        else:
            print("i am happy")

        self.__clock()

def main():
    petName = input("what is your pet name? ")
    petType = input("what type of animal is your pet? ")

    p1 = Pet(petName, petType)
    input("hola, i am " + p1.name + " and i am new here" + "\n press enter to start")

    choice = ""
    while choice != "0":
        print("\n 1- feed your pet \n 2- talk with your pet \n 3- teach your pet new word \n 4- play with your pet \n 0- quit")

        choice = input("choice: ")
        if choice == "0":
            print("good bye")
        elif choice == "1":
            p1.feed()
        elif choice == "2":
            p1.talk()
        elif choice == "3":
            new_word = input("what do you want to teach it to say? ")
            p1.teach(new_word)
        elif choice == "4":
            p1.play()
        else:
            print("sorry.. this is not a valid option")

main()
