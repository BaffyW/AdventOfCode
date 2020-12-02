import re

alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
#inFile = open("input.txt")
inFile = open("passwords.txt")
data = []
"""for line in inFile:
    data.append(line)"""

def validPassword():
    min = 0
    max = 0
    seek = ''
    password = ""

    count = 0
    for line in inFile:
        #Find lower and upper bounds
        temp = re.findall(r'\d+', line)
        res = list(map(int, temp))
        """min = res[0]
        max = res[1]"""
        min = res[0] - 1
        max = res[1] - 1

        letters = []
        for obj in line:
            if(obj in alphabet):
                letters.append(obj)
        seek = letters[0]
        password = letters[1:]
        
        """found = 0
        #Find occurences of letter in password.
        for letter in password:
            if (seek == letter):
                found +=1"""
        
        #Count if the occurences fit the limits.
        """if(min <= found and found <=max):
            count +=1"""
        
        #Count if the letter occurs on only one of the specified positions.
        if ((password[min] == seek) != (password[max] == seek)):
            count +=1
        

        #print(min, max, seek, password, found)
    print(count)
    
validPassword()