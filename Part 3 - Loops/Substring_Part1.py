#Please write a 
#program which asks the user to 
#type in a string. 
#The program then prints out all the 
#substrings which begin 
#with the first character, 
#from the shortest to the longest.
word = input("Please type in a string:")
wordIndex = 0
stop =  len(word) + 1

while wordIndex != stop :
    
    print(word[:wordIndex])
    wordIndex += 1
