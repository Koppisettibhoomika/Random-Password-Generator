import string
import random

passLen = int(input("Enter password length as per your choice: "))

print('''prefer any character set for password of your choice :
		1. Letters or alphabets
		2. symbols or special characters
		3. numbers
		4. Exit''')

characters = " "
while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		
		characters += string.ascii_letters
	elif(choice == 2):
		
		characters += string.punctuation
	elif(choice == 3):
		
		characters += string.digits
	elif(choice == 4):
		break
	else:
		print("Please pick a valid option for generating a password!")

passwordGenerated = []

for i in range(passLen):

	randomchoice = random.choice(characters)
	
	passwordGenerated.append(randomchoice)

print("The random password of your choice is like " + "".join(passwordGenerated))
