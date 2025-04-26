name='Dursikshya Education Network.' 

#len(): calculate length of string 
length=len(name)
print(length)
print(name[28])

print(name.lower())
print(name.upper())
print(name.title()) #shows first letter of all words capital
print(name.capitalize()) # shows first letter captial only

#split(sep='')
print(name.split()) # to make list
print(name.split(',')) 

print(name.count('a')) # to count the letter,words,etc
print(name.count('D')) 
print(name.count('ti')) 

print(name.replace('a','A')) # old value ,new value

word= input('enter your word')
print(word,len(word))

print(word.strip()),len(word.strip())  #removes wide space

print(word.lstrip()),len(word.lstrip())  # removes wides space from left side

#find() : it helps to find indexing value of given substring.

print(name.find('sikshya')) #to find the letter
print(name.index('Edu'))

print(name.islower())
print(name.istitle())

n='1234'
print(n.isnumeric())

n='1234.44'
print(n.isnumeric())

#for item in name: #in sequence
    #print(item)

count=0
vowel=['a','e','i','o','u']
for letter in name:
    if letter.lower() in vowel:
        count+=1
    
print('total vowel letter is',count)








