
# Get inputs from user

print("Hi! I need a couple of inputs from you to make your experience jovial. So let's start then by hitting ENTER :)")
name1 = input("Name: ")
nickname = input("Nick Name: ")
adjective1 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_character1 = input("Famous Character: ")
he_she = input("He/She: ")
pronoun1 = input("Pronoun: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
verb3 = input("Verb: ")
adjective2 = input("Adjective: ")
sound = input("Sound: ")
famous_character2 = input("Famous Character: ")
noun4 = input("Noun: ")

paragraph = f"""
	Hello peeps! Let me introduce you to myself first, my name is {name1}, people often call me
	as {nickname}. I am a very {adjective1} person and I love to {verb1}. Although I don't {verb1} daily but
	I prefer to {verb1} quite often on and off basis.

	Have you ever heard about {famous_character1}? {he_she} is a very nice {noun1}. I used to play {noun2} with
	{pronoun1}. Last night I cooked {noun3} for {pronoun1} and believe me {noun1} was blown out of {verb3}.
	Haha...! {adjective2} right?

	{sound}...!!!

	Well..
	{famous_character2} is calling me, gotta go now.
	Thanks for your time {noun4}!
	You are a lovely person.
	Have a great day mate!
"""

print(paragraph)