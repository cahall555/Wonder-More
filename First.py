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
#quote with space and new lines
print("\n\n\tBlack care rarely sites behind a rider whose pace is fast enough. \n\t\t\t ~Theodore Roosevelt")
#variable testing title() upper() lower()
president = "theodore roosevelt"
print(president)
print(president.title())
print(president.upper())
print(president.lower())
#variable testing strip with title
president_l = " abraham lincolin "
print(president_l.title().strip())
print(president_l.title().lstrip())
print(president_l.title().rstrip())
#testing user input function
myname = input("Enter your name: ")
print("Hello, ", myname.title(),"!")





	

