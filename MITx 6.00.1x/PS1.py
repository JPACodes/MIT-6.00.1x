#Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels
# contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

#Solution 1 (pythonic)
# s = 'azcbobobegghakl'
# vowels = ['a' , 'e' , 'i' , 'o' , 'u']
# vowelcount = 0
# for i in range(len(s)):
#    if s[i] in vowels:
#        vowelcount += 1
#    else:
#        pass
#
# print(vowelcount)

#Solution 2 (Algorithmic)
s = 'azcbobobegghakl'
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
vowelcount = 0

for i in range(len(s)):
    for j in range(len(vowels)):
        if s[i] == vowels[j]:
            vowelcount += 1
        else:
            pass

print(vowelcount)