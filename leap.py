
user_input = input("Enter year :(ex. 1998) ")
array = []
for i in user_input:
	array.append(i)

def leap(year):
	if year[-1] and year[-2] == 0:
		if int(user_input) % 400 == 0:
			print("This year is leap")
		else:
			print("This year is not leap")
	else:
		if int(user_input) % 4 == 0:
			print("This year is leap")
		else:
			print("This year is not leap")


leap(array)