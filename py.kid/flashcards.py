#Flashcard game
#First ask user how many flashcards they want to enter.
#Then loop through desired quantity
fc_num = int(input("How many flashcards would you like to make?"))
a = int(1)

while (a <= fc_num):
	print("Card %s of %s" % (a,fc_num))
	class myclass:
	side1 = input("what would you like on side 1?")
	side2 = input("what would you like on side 2?")
	a = a + 1

# what order would you like the cards, suffled, not shuffled
#then print the cards

print(side1)
print(side2)
