from array import *

alphabet="abcdefghijklmnopqrstuvwxyz$"
alphabet=(list(alphabet))


#print (alphabet[25])
#print(alphabet.index("y"))
badscore=''
badscore=list(badscore)
def decode():
    global badscore
    message = input('\n Введите своё сообщение: ')
    newmessage=list(message)
    for i in range (len(message)):
        if newmessage[i]==' ':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='1':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='2':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='3':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='4':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='5':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='6':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='7':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='8':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='9':
            newmessage[i]='$'
            badscore+=str(i)
        if newmessage[i]=='0':
            newmessage[i]='$'
            badscore+=str(i)
    badscore=''
    
    badscore=list(badscore)
    print (badscore)
    for j in range (len(newmessage)):
        if newmessage[j]=='$':
            print(j)
            
            badscore.append(str(j))
    print (badscore)
    
    for i in range (len(badscore)):
        etoudali=badscore[i]
        print("Это надо удалить",etoudali)
        newmessage.remove('$') 
              
            
        
    print (newmessage)
   
    message,newmessage=newmessage,message
    key=input('\n Введите ключ: ')
    skolko=round((len(message)/len(key)))+1
    print(skolko)
    key*=skolko
    print(key)
    newkey=''
    for i in range (len(message)):
        newkey+=key[i]
    key=str(newkey)
    print (key)

    def getcodsmessage():
        codemessage=''
        for i in range(len(key)):
            codemessage+=" "
        codemessage= list(codemessage)

        for i in range (len(message)):
            #print (key[i])
            leter = key[i]
            leter = alphabet.index(leter)
            #print (leter)
            codemessage[i]= str(leter)
            #print (codemessage)
        return codemessage

    def getcodskey():
        codekey=''
        for i in range(len(key)):
            codekey+=" "
        codekey= list(codekey)

        for i in range (len(key)):
            #print (message[i])
            leter = message[i]
            leter = alphabet.index(leter)
            #print (leter)
            codekey[i]= str(leter)
            #print (codekey)
        return codekey


    codemessage = getcodsmessage()
    codekey = getcodskey()
    codemessage , codekey = codekey, codemessage

    print (codemessage)
    print (codekey)
    shifr=''
    for i in range(len(key)):
        shifr+=" "
    shifr=list(shifr)    
    for i in range(len(message)):

        if ((int(codemessage[i])-int(codekey[i]))<0):
            #print ("Ploho", i)
            shifr[i]=(str((int(codemessage[i])+26-int(codekey[i]))))

        else:
           #print(str((int(codemessage[i])+int(codekey[i]))))

           shifr[i]=(str((int(codemessage[i])-int(codekey[i]))))
    print (str(shifr))
    visibleshifr=''
    for i in range (len(shifr)):
        number = shifr[i]
        number = int(number)
        visibleshifr+=alphabet[ number ]
    visibleshifr=list(visibleshifr)
    for i in range (len(badscore)):
        #print ("Вот на этих позициях ошибки:", badscore)
        numbererror=int((badscore[i]))
        #visibleshifr[int((badscore[i]))]=newmessage[numbererror]
        x=int((badscore[i]))
        y= ((newmessage[x]))
        print (x)
        print (y)
        
        visibleshifr.insert(x,y) 
        
        
    newvisibleshifr=''
    for i in range (len(visibleshifr)):
        newvisibleshifr+=visibleshifr[i]
    print ('Вот твой РАСшифрованный сообщение',str (newvisibleshifr))

decode()