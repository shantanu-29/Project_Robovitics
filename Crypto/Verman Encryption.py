#Key length can be lesser than the plaintext length. So it is taken till key is exhausted


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
    key=key.replace(" ", "")
    key=key.lower()
    text=input("Enter the Plain text: ")
    text=text.replace(" ", "")
    text=text.lower()
    l1=[]
    l2=[]
    for i in key:
        for j in alphabet_to_number_dict:
            if(i==j):
                l1.append(alphabet_to_number_dict.get(j))

    for i in text:
        for j in alphabet_to_number_dict:
            if(i==j):
                l2.append(alphabet_to_number_dict.get(j))

    l=int(len(key))
    new=[]
    for i in range(l):
        ele1=int((l1[i]+l2[i])%26)
        new.append(ele1)

    l2=new+l2[l:]
    #print(l2)

    cipher_text=""
    for i in l2:
        for j in number_to_alphabet_dict:
            if(i==j):
                cipher_text=cipher_text+ number_to_alphabet_dict.get(j)

    print("The Encrypted text is: ",cipher_text.upper())


def Decrypt():
    key=input("Enter the key: ")
    key=key.replace(" ", "")
    key=key.lower()
    text=input("Enter the Cipher text: ")
    text=text.replace(" ", "")
    text=text.lower()
    l1=[]
    l2=[]
    for i in key:
        for j in alphabet_to_number_dict:
            if(i==j):
                l1.append(alphabet_to_number_dict.get(j))
    print(l1)
    for i in text:
        for j in alphabet_to_number_dict:
            if(i==j):
                l2.append(alphabet_to_number_dict.get(j))

    l=int(len(key))
    new=[]

    for i in range(l):
        if int(l2[i]-l1[i])>=0:
            ele1=int((l2[i]-l1[i])%26)
            new.append(ele1)
        else:
            ele1=int(l2[i]-l1[i])+26
            new.append(ele1)
    l2=new+l2[l:]

    plain_text=""
    for i in l2:
        for j in number_to_alphabet_dict:
            if(i==j):
                plain_text=plain_text+ number_to_alphabet_dict.get(j)
    print(plain_text.upper())

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






