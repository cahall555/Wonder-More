print("Hello World!")
#build a list
shoplist = []
shoplist.append("Bread")
shoplist.append("Milk")
shoplist.append("Butter")
shoplist.append("Apples")
print(shoplist)
#try a function
def first_function():
	print("Hello From First Function!")
print(first_function)
#create a dictionary
first_dictionary = {
	"Operouse" : "tedious",
	"Callow" : "lacking adult sophistication",
	"Gamification" : "the process of adding games",
	"Prestidigitation" : "slide of hand"
}
print(first_dictionary)
#for loop
for word, definition in first_dictionary.items():
	print("The word of the day is %s : %s" % (word, definition))
	

