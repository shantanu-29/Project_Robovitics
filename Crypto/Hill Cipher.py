#Key inputted in NXN matrix format. Plaintext divided into 1XN row matrix and multiplied with Key matrix.
#If it is more than 25 then modulus 26 is taken and converted to corresponding alphabet(ciphertext)


import numpy as np
from sympy import Matrix
number_to_alphabet_dict = { 0:'a',1:'b',2:'c',3:'d',4:'e'
                           ,5:'f',6:'g',7:'h',8:'i',9:'j'
                           ,10:'k',11:'l',12:'m',13:'n',14:'o'
                           ,15:'p',16:'q',17:'r',18:'s',19:'t'
                           ,20:'u',21:'v',22:'w',23:'x',24:'y'
                           ,25:'z'}

alphabet_to_number_dict = {  'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4
                           , 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9
                           , 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14
                           , 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19
                           , 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24
                           , 'z': 25}


def Encrypt():
    key=input("Enter the key: ")
    key=key.replace(" ", '')
    key=key.lower()
    key1=[]
    for a in key:
        for b in alphabet_to_number_dict:
            if(a==b):
                key1.append(alphabet_to_number_dict.get(b))
    mat=[]
    x=0;
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(key1[x])
            x=x+1
        mat.append(row)
    plain_text=input("Enter the plain text: ")
    plain_text=plain_text.replace(" ", "")
    plain_text=plain_text.lower()
    if(len(plain_text)%3!=0):
        if(len(plain_text)%3==1):
            plain_text=plain_text[:]+'x'+'x'
        else:
            plain_text=plain_text[:]+'x'
    l=[]
    for i in plain_text:
        for j in alphabet_to_number_dict:
            if(i==j):
                l.append(alphabet_to_number_dict.get(j))
    ctr=int(len(plain_text)/3)
    cipher_text=""
    for i in range(0,len(l),3):
        b=[l[i],l[i+1],l[i+2]]
        P=[0,0,0] 
        C=[]
        P = np.dot(mat,b)
        for r in P:
            x=r%26
            C.append(x)
        for i in C:
            for j in number_to_alphabet_dict:
                if(i==j):
                    cipher_text=cipher_text[:]+ number_to_alphabet_dict.get(j)
    print("The Cipher text is: ")
    print(cipher_text.upper())

def Decrypt():
    key=input("Enter the key: ")
    key=key.replace(" ", '')
    key=key.lower()
    key1=[]
    for a in key:
        for b in alphabet_to_number_dict:
            if(a==b):
                key1.append(alphabet_to_number_dict.get(b))
    mat=[]
    x=0;
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(key1[x])
            x=x+1
        mat.append(row)

    text=input("Enter the text to be decrypted: ")
    text=text.lower(); 
    D=[]
    for i in text:
        for j in alphabet_to_number_dict:
            if(i==j):
                D.append(alphabet_to_number_dict.get(j))
    text1=""
    for i in range(0,len(D),3):
        v=[[D[i]],[D[i+1]],[D[i+2]]]
        l3=[]
        S = Matrix(mat).inv_mod(26)
        T=np.dot(S,v)
        for i in T:
            y=i%26
            l3.append(y)
        for i in l3:
            for j in number_to_alphabet_dict:
                if(i==j):
                    text1=text1[:]+number_to_alphabet_dict.get(j)
    print("The Plain text is: ")
    print(text1.upper())

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n"))
    if choice==1:
        Encrypt()
    elif choice==2:
        Decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")