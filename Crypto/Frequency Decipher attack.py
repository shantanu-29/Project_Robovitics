count = {  'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0
        ,  'f': 0, 'g': 0,  'h': 0, 'i': 0, 'j': 0
        , 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0
        , 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0
        , 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0
        , 'z': 0}

check = {  'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5
        ,  'f': 6, 'g': 7,  'h': 8, 'i': 9, 'j': 10
        , 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15
        , 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20
        , 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25
        , 'z': 26}

number_to_alphabet_dict = { 1:'a',2:'b',3:'c',4:'d',5:'e'
                           ,6:'f',7:'g',8:'h',9:'i',10:'j'
                           ,11:'k',12:'l',13:'m',14:'n',15:'o'
                           ,16:'p',17:'q',18:'r',19:'s',20:'t'
                           ,21:'u',22:'v',23:'w',24:'x',25:'y'
                           ,26:'z'}


str1=input("Enter the string: ")
str1=str1.lower()
for i in str1:
    for j in count:
        if(i==j):
            count[j]=count.get(j)+1
#print(count)
test=0
alphabet=""
for i in count:
    if int(test)<count.get(i):
        test=count.get(i)
        alphabet=i

print("Alphabet with highest frequency: ",alphabet)
#print(test)
for i in check:
    if alphabet==i:
        position=check.get(i)
#print(position)
shift=int(position -5)
print("The shift is: ",shift)

l1=[]
for i in str1:
        for j in check:
            if(i==j):
                l1.append(((check.get(j)-shift)+26)%26)
    
#print(l1)
#print("\n")
final=''
for i in l1:
    for j in number_to_alphabet_dict:
        if(i==j):
            final=final+ number_to_alphabet_dict.get(j)
print("The decrypted text is\n")
print(final.upper())
print("\n")
print("Want to try again  Y/N:")
