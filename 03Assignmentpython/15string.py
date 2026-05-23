#Write a Python program that allows the user to search for a character within a
#given string.


user=input("Enter the character ")
search=input("Enter the search ")
for i in user:
    if i == search:
        print(i)
