import time
import random
from decimal import Decimal, ROUND_DOWN
from os import system
system('clear')
print ("Hello and welcome to Maths Tester Pro!")
testcode = input("Please enter your test code: ")
studentname = input("Please enter your name: ")
print(f"Hello {studentname}!")
testparameters = testcode.split("|")
testlength = int(testparameters[0])
testoperator = testparameters[1]
if testoperator == "*":
	testoperator = "x"
testrange1 = int(testparameters[2])
testrange2 = int(testparameters[3])+1
score = 0
for qe in range(0,testlength):
	equationint1 = random.randint(testrange1,testrange2)
	equationint2 = random.randint(testrange1,testrange2)
	questionattempt = input(f"{equationint1} {testoperator} {equationint2}: ")
	if testoperator == "+":
		answer = (equationint1+equationint2)
		if int(questionattempt) == answer:
			print ("Well done! You got the answer correct.")
			score = score+1
			input("Press enter when you are ready to move onto the next question...")
			system('clear')
		else:
			print (f"Oh dear! Better luck next time. The answer was {answer}")
			input("Press enter when you are ready to move onto the next question...")
			system('clear')
	elif testoperator == "-":
		answer = (equationint1-equationint2)
		if int(questionattempt) == answer:
			print ("Well done! You got the answer correct.")
			score = score+1
			input("Press enter when you are ready to move onto the next question...")
			system('clear')
		else:
			print (f"Oh dear! Better luck next time. The answer was {answer}")
			input("Press enter when you are ready to move onto the next question...")
			system('clear')
	else:
		answer = (equationint1*equationint2)
		if int(questionattempt) == answer:
			print ("Well done! You got the answer correct.")
			score = score+1
			input("Press enter when you are ready to move onto the next question...")
			system('clear')
		else:
			print (f"Oh dear! Better luck next time. The answer was {answer}")
			input("Press enter when you are ready to move onto the next question...")
			system('clear')

rawpercentage = score/testlength*100	
styledpercentage = Decimal(rawpercentage).quantize(Decimal('00'),  rounding=ROUND_DOWN)	
print (f"""Well done for completing this test {studentname}!
Here are your results:
Score: {score}/{testlength}
Percentage: {styledpercentage}%
""")
