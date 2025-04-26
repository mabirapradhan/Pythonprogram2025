# dictionary
# unordered collection of elements having key:value,separeted by comma(,) and enclosed by {}
# it is mapping data type structure.

#initialise/ empty dictionary

abc={}
print(abc,type(abc))

books=['eng','nepali']
books[0]

std={
    'name':'mabira',
    'address':'ktm',
    'profession':'student',
    'class' :10
}

print(std,type(std))

# accessing ,indexing and slicing

print(std['address'])
print(std.get('name'))

print(len(std))

print(books[0])

#update list
books[0]='English'
print(books)

#updarw dictionary
std['address']='Kathmandu'
print(std)

print(std.items()) #items displays all keys and values

print(std.keys()) #.keys diplays keys only

print(std.values()) #.values diplays values only

print(std.pop('class')) # .pop removes items from required key

#removing items from last position
print(std.popitem())

#loop in dictionary
# for i in books:
# print(i)

for k,v in std.items():
    print(k,v)

for key in std.keys():
    print(std[key])

# ADDING ELEMENTS IN DICTIONARY
abc['dicstrict']='kathmandu'
print(abc)

abc['country']='nepal'
print(abc)


# create a dictionary having general detail of yours and one key having list of courses you enrolled.

course=[]
detail={
    'name':'mabira',
    'address':'ktm',
    'profession':'student',
    'course':['python','maths','violin']
    }
print(detail.items())

# wap to store values with their frequency found in string.

words='python is easy language and python is powerful language'
# w=words.split()
# print(w)

word_count={}
for word in words.split(): #['python','is','easy','language','and','pyhton','is','powerful','language]
    if word in word_count.keys(): 
        word_count[word]+=1 
    else:
        word_count[word]=1
    
print(word_count)


word_count={}
for word in words.split():
    print(words.split())
    if word in word_count.keys(): 
        word_count[word]+=1
    else:
        word_count[word]=1
    print(word_count)


#nested list,dict,and combine

list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

final_list=[list1,list2,list3]
print(final_list)

print(final_list[1])
print(final_list[1][1])

# nested dictionary

std={
    'key1':{
            'key2':{
                'key3':'value'
            }
        }
    }

print(std['key1'])
print(std['key1']['key2'])
print(std['key1']['key2']['key3'])

# wap to display student name as key and marks as value in dictionary from a dictionary having keys names
# marks,and their respective values have list of name and list of marks,where student scored above 60 percent.
# both list must be sam elength respective indexs are combined.
new={}
dict={
    'name':['leeza','rohit','mabira','bibhuti','karan'],
    'marks':[45,98,85,64,23]
}
print(dict)

for i in range(len(dict['name'])):
    if dict['marks'][i]>60:
        new[dict['name'][i]] =dict['marks'][i]

print(new)
       
        

