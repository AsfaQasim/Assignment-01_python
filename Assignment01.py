# 1
full_name = "AsFa QAsim"
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

#  Output

# Asfa Qasim
# ASFA QASIM
# asfa qasim

#  2

mixed_text = " This text is messed up! "
print(mixed_text.strip(), "This text is remove whitespace...")
print(mixed_text.replace("up", "down"), "Up replace with down")
print(mixed_text.strip().count("i"), " ...i in the string")
print(mixed_text.split(), "This text is chnage into list")

#  Output

# This text is messed up! This text is remove whitespace...
#  This text is messed down!  Up replace with down
# 2  ...i in the string
# ['This', 'text', 'is', 'messed', 'up!'] This text is chnage into list


#  3

sentence = "quicK brown fox over the lazy dog!"
print('_'.join(sentence.split()))
print(sentence.startswith("the"))
print("The position of word fox in the senetence is ...", sentence.find("fox"))


#  Output

# quicK_brown_fox_over_the_lazy_dog!
# False
# The position of word fox in the senetence is ... 12

#  input

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert age to integer
fav_programming_lan = input("Enter your favourite programming language: ")

message = f"My name is {name}, my age is {age}, and my favourite programming language is {fav_programming_lan}."
message2 = f"In 5 years, I will be {age + 5} years old."

print(message)
print(message2)

#  Output

# Enter your name: asfa
# Enter your age: 22
# Enter your favourite programming language: ts
# My name is asfa, my age is 22, and my favourite programming language is ts.
# In 5 years, I will be 27 years old.

#  part 04

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2025

print(first_name.capitalize())
print(last_name.capitalize())

age = current_year - birth_year
username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"

profile_message = f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}"

print(profile_message)

#  Output

# Enter your first name: asfa
# Enter your last name: qasim
# Enter your birth year: 2001
# Asfa
# Qasim
# Profile: asfa qasim, Age: 24, Username: aqasim2001