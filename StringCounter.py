print("")
print("    ***** same string counter *****")
print("")
string = input("Enter any String : ")
string = list(string)
print("")
n = 0
catCount = 0
dogCount = 0
while n != len(string):
    if string[n] == 'c' or string[n] == 'C':
        n = n + 1
        if string[n] == 'a' or string[n] == 'A':
            n = n + 1
            if string[n] == 't' or string[n] == 'T':
                n = n + 1
                catCount = catCount + 1
    elif string[n] == 'd' or string[n] == 'D':
        n = n + 1
        if string[n] == 'o' or string[n] == 'O':
            n = n + 1
            if string[n] == 'g' or string[n] == 'G':
                n = n + 1
                dogCount = dogCount + 1
    else:
        n = n + 1

if catCount == dogCount:
    print("True!!")
    print("Because there are "+ str(catCount) + " number of cat and " + str(dogCount) +" number of dog in the given string.. ")
else:
    print("False!!")
    print("Because there are not equal numbers, "+ str(catCount) +" number of cat and "+ str(dogCount) +" number of dog in the given string.. ")




