#Key stored in 5X5 matrix without repeatation, Plaintext broken in pairs with no repeatations.
#The pairs are checked in the matrix and encrypted accordingly.


def Encrypt():  
    alphabets="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key=input("Enter key: ")
    key=key.replace(" ", "")
    key=key.upper()
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)] 
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    for i in alphabets:
        if i not in result:
                result.append(i)

    k=0
    my_matrix=matrix(5,5,0)
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    def locindex(c):
        loc=list()
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc 
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                 msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:")
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2
def Decrypt():
    alphabets="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key=input("Enter key: ")
    key=key.replace(" ", "")
    key=key.upper()
    def matrix(x,y,initial):
        return [[initial for i in range(x)] for j in range(y)] 
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    for i in alphabets:
        if i not in result:
                result.append(i)

    k=0
    my_matrix=matrix(5,5,0)
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1
    def locindex(c):
        loc=list()
        if c=='J':
            c='I'
        for i ,j in enumerate(my_matrix):
            for k,l in enumerate(j):
                if c==l:
                    loc.append(i)
                    loc.append(k)
                    return loc  
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("\nPLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2    

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