#Key length can be lesser than plaintext. Thus Key is repeated till the entire plaintext is covered.

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
key=input("Enter the key: ")
key=key.lower()
key1=[]
for i in key:
        for j in alphabet_to_number_dict:
            if(i==j):
                key1.append(alphabet_to_number_dict.get(j));
def Encrypt():
    plain_text1=[]
    plain_text=input("Enter the plain text: ")
    plain_text=plain_text.lower()
    for i in plain_text:
        for j in alphabet_to_number_dict:
             if(i==j):
                 plain_text1.append(alphabet_to_number_dict.get(j));
    cipher_text=[]
    b=0
    for a in plain_text1:
        if(b==len(key1)):
            b=0;
            ele=(a+key1[0])%26
            cipher_text.append(ele)
            b=b+1
        else:
            ele=(a+key1[b])%26
            cipher_text.append(ele)
            b=b+1
    cipher_text1=""
    for i in cipher_text:
        for j in number_to_alphabet_dict:
            if(i==j):
                cipher_text1=cipher_text1+number_to_alphabet_dict.get(j)
    print("The Encrypted text is : ",cipher_text1.upper())

def Decrypt():
    ciphered_text1=[]
    ciphered_text=input("Enter the ciphered text: ")
    ciphered_text=ciphered_text.lower()
    for i in ciphered_text:
        for j in alphabet_to_number_dict:
            if(i==j):
                 ciphered_text1.append(alphabet_to_number_dict.get(j));
    c=0;
    ciphered_text2=[]
    for a in ciphered_text1:
        if(c==len(key1)):
            c=0
            if(a-key1[c]<0):
                ele=(a-key1[c]+26)%26
                ciphered_text2.append(ele)
                c=c+1 
            else:
                ele=(a-key1[c])%26
                ciphered_text2.append(ele)
                c=c+1
        else:
            if(a-key1[c]<0):
                ele=(a-key1[c]+26)%26
                ciphered_text2.append(ele)
                c=c+1 
            else:
                ele=(a-key1[c])%26
                ciphered_text2.append(ele)
                c=c+1   
    final=""
    for i in ciphered_text2:
        for j in number_to_alphabet_dict:
            if(i==j):
                final=final+number_to_alphabet_dict.get(j)
    print("The plaintext is : ",final.upper())
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