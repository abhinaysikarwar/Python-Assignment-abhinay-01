# Given: text = "python programming"
#Goal: Count how many vowels are in the string.
#Constraint: Do not use indexing (text[i]) or slicing (text[:]).


text = "python programming"
count=0
for i in text:
    if i in "aeiouAEIOU":
        count=count+1
print(count)