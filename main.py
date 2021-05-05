#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# password=""
# for no_of_letters in range(1,nr_letters+1) :
#   unit= random.randint(0,nr_letters+1)
#   password += letters[unit]
# for no_of_symbols in range(1,nr_symbols+1) :
#   unit2= random.randint(0,nr_symbols+1)
#   password += symbols[unit2]
# for no_of_numbers in range(1,nr_numbers+1) :
#   unit3=random.randint(0,nr_numbers+1)
#   password += numbers[unit3]
# print(password)


password_list=[]
for no_of_letters in range(1,nr_letters+1) :
  unit= random.randint(0,nr_letters+1)
  password_list.append(letters[unit]) 
for no_of_symbols in range(1,nr_symbols+1) :
  unit2= random.randint(0,nr_symbols+1)
  password_list.append( symbols[unit2])
for no_of_numbers in range(1,nr_numbers+1) :
  unit3=random.randint(0,nr_numbers+1)
  password_list.append( numbers[unit3])

random.shuffle(password_list)
password=""
for list in password_list :
  password += list
print(password)
  