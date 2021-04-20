# Import Libraries
from time import sleep
from os import system
from random import randrange


# Database to store customer details
database = {}


# Initialization
def init():
	print("Welcome to BankPHP")
	haveAccount = int(input("Do you have account with us: (1) yes (2) no\n"))
	if haveAccount == 1:
		Login()
	elif haveAccount == 2:
		Register()
	else:
		print("You selected an invalid option")
		init()


#Registration
def Register():
	print("**********Register*************")
	firstName = input("Enter your first name: ")
	while not firstName.isalpha():
		print("Name cannot contain numeric and characters")
		firstName = input("Enter your first name: ")

	lastName = input("Enter your last name: ")
	while not lastName.isalpha():
		print("Name cannot contain numeric and characters")
		lastName = input("Enter your last name: ")

	email = input("Enter your email address: ")
	while not('@' in email and email[0]!='@'):
		print("Enter a valid email address")
		email = input("Enter your email address: ")

	password = input("Enter a password: ")

	#Generate account number
	accountNumber = AccountGenerator()
	database[accountNumber] = [firstName, lastName, email, password,0] #  0 is the initial balance of the user
	print("\nAccount created successfully")
	print("\nYour account number is: %s" %accountNumber)
	firstTime = int(input("\nDo you want to login? (1) yes (2) no : "))
	while firstTime != 1 or firstTime != 2:
		if firstTime == 1:
			Login()
		elif firstTime == 2:
			init()
		else:
			print("you selected a wrong option!")
			firstTime = int(input("\nDo you want to login? (1) yes (2) no : "))


#Login
def Login():
	print("********Login********")
	userAccountNumber = input("Enter your account number: ")
	userID = input("Enter your password: ")

	for accountNumber,userDetails in database.items():
		if (accountNumber == userAccountNumber and userDetails[3] == userID):
			BankOperation(userDetails)
		else:
			print("Invalid account number or password")
			print("press 0 to quit or any number to login")
			opt = int(input())
			if opt == 0:
				quit()
			else:
				Login()


#Generate Account
def AccountGenerator():
	first = "0"  # All account numbers generated to start with 0
	others = randrange(111111111,999999999)
	account = first + str(others)
	return account


#Waiting
def Processing():
	print("Transaction processing.\r", end='')
	sleep(1)
	print("Transaction processing..\r", end='')
	sleep(1)
	print("Transaction processing...")


def another(user):
	again = int(input("Do you want to do another transaction? (1) yes (2) no: "))
	if again == 1:
		BankOperation(user)
	elif again == 2:
		Logout()
	else:
		print("you selected a wrong option!")
		another()


def BankOperation(user):
	print("Welcome %s %s \n" % ( user[0], user[1] ) )
	print("What do you want to do\n")
	print("1. Withdraw				2. Deposit")
	print("3. Check Balance		    4. Customer Service")
	print("5. Logout				6. quit")

	selectedOption = int(input("Enter selection: "))

	if selectedOption == 1:
		withdrawalOperation(user)
		another(user)

	elif selectedOption == 2:
		depositOperation(user)
		another(user)

	elif selectedOption == 3:
		checkBalance(user)
		another(user)

	elif selectedOption == 4:
		customerService(user)
		another(user)

	elif selectedOption == 5:
		Logout()

	elif selectedOption == 6:
		quit()

	else:
		print("Invalid option selected")
		BankOperation(user)


def withdrawal(user,amount):
	if user[4] > amount:
		Processing()
		print("Take your cash")
		user[4] -= amount
		print("Your balance is %d" %user[4])
	else:
		print("Insufficient balance")


def withdrawalOperation(user):
	print("How much do you want to withdraw\n")
	print("1. 1000		4. 10000")
	print("2. 2000		5. 20000")
	print("3. 5000		6. others")

	selection = int(input())
	if selection == 1:
		withdrawal(user, 1000)

	elif selection == 2:
		withdrawal(user, 2000)

	elif selection == 3:
		withdrawal(user, 5000)

	elif selection == 4:
		withdrawal(user, 10000)

	elif selection == 5:
		withdrawal(user, 20000)

	elif selection == 6:
		other = float(input("Enter amount to witdraw: "))
		withdrawal(user, other)


def depositOperation(user):
	deposit = float(input("Enter amount to deposit: "))
	user[4] += deposit
	print("Your balance is %.2f" %user[4])
	


def checkBalance(user):
	print("Your balance is %.2f" %user[4])


def Logout():
	print("Thank you for banking with us")
	sleep(3)
	system("clear")
	init()


def customerService(user):
	print("Dear %s %s" %(user[0], user[1]))
	print("What is your complaint: ")
	complaint = input()
	print("Thank you for contacting us, we will get back to you")

	
# ATM Banking Service
init()






