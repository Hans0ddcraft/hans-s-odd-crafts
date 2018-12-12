#The alphabet
al = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
#The Numbers
num = '0 1 2 3 4 5 6 7 8 9 '
#Turn the strings into lists
al = al.split()
num = num.split()
#The loop to run the program
while True:
    #Set the output string
    output = []
    #User inputs the mode
    mode = input('Select which mode you want:[decode or encode] ').lower()
    #Encode
    if mode == 'encode':
        this = input('Enter a string to be encoded.').lower()
        for i in this:
            if i in al and (i != 'y' and i != 'z'):
                output.append(al[al.index(i)+2])
            elif i == 'y':
                output.append(al[0])
            elif i == 'z':
                output.append(al[1])
            elif i == '8':
                output.append(num[0])
            elif i == '9':
                output.append(num[1])
            elif i in num:
                output.append(num[num.index(i)+2])
            else:
                output.append(i)
        output= ''.join(output)
        print(output)
        yes = input('Do you wish to run the program again?').lower()
        if yes != 'yes':
            break
    #Decode
    elif mode == 'decode':
        this = input('Enter a string to be decoded.').lower()
        for i in this:
            if i in al and (i != 'y' and i != 'z'):
                output.append(al[al.index(i)-2])
            elif i == 'y':
                output.append(al[-2])
            elif i == 'z':
                output.append(al[-1])
            elif i == '8':
                output.append(num[-2])
            elif i == '9':
                output.append(num[-1])
            elif i in num:
                output.append(num[num.index(i)-2])
            else:
                output.append(i)
        output= ''.join(output)
        print(output)
        yes = input('Do you wish to run the program again? ').lower()
        if yes != 'yes':
            break
    else:
        #If the mode was invalid as in not matching the strings 'encode' or 'decode'
        print("That wasn't a valid mode")
            
    
    