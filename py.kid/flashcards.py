
from kivy.app import App

class FcApp (App):
    #Flashcard game
    #First ask user how many flashcards they want to enter.
    #To loop through desired quantity
    fc_num = int(input("How many flashcards would you like to make?"))
    a = int(1)

    #setup empty dictionary to hold side one and side 2 of flash cards
    fc_dictionary = {}

    #After getting the number of flashcards a user wants dictionary loop should
    #loop user through adding flascards.  
    while (a <= fc_num):
        print("Card %s of %s" % (a,fc_num))
        k = raw_input("what would you like on side 1? ")
        v = raw_input("what would you like on side 2? ")
        fc_dictionary[k] = v
        a = a + 1

    #print out flashcards so user see entries
    for key, value in fc_dictionary.items():
        print("\nSide 1: " + key)
        print("Side 2: " + value)

if __name__ == '__main__':
    FcApp().run()
# what order would you like the cards, suffled, not shuffled
#then print the cards




