#kids fill in the blank and choose your own adventure story

#Declare variables for story, all input variables to be a part of the story
animal = input("Enter your favorite animal name: ")
main_char = input("Enter a name: ")
animal_name = input("Enter another name: ")
activity = input("Enter an activity (as verb): ")
food = input("Enter a food: ")

#story
print("\n\tOnce upon a time there was a little girl named",main_char.title(), "who had pet ",
animal,". She named her",animal,animal_name.title(),".",main_char.title(), "and",animal_name.title(),"did everything together. They especially enjoyed",activity,
"and eating",food,"together.\n\tOne day while out",activity,main_char.title(),"and",animal_name.title(),"became separated.")

#insert first branch/user choice here
separated = input("What would you do? Go home and look or stay where you are?")
if "home" in separated:
	print("\n\t", main_char.title(), "decided to",separated,". On the way home",main_char.title(), "ran into a friend )
elif "stay" in separated:
	print("\n\t", main_char.title(), "decided to",separated,".")

