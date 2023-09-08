def conson():
    #create an empty string called result 
    result = ""
    #create vowel tuple to counter check  with the entered string
    vowels =("a", "e", "i", "o", "u")
    #initialize the value of consonant to zero 
    cons_value = 0
     #initialize the value of maximum to zero 
    max_value = 0
    #prompts the user to enter values
    user = input("Enter String:" + " ")
    #iterates through given string and converts to lower case
    for char in user.lower():
        #checks if the charact in a given string exist in a given tuple if it exist it omits
        if char not in vowels: 
            # final string without vowels          
            result = result + char  
            #the formula below gives numeric representation of a character
            #calculates the value of the current consonant character based on its position 
            # in the alphabet and adds it to the accumulated 
            cons_value += ord(char) - ord('a') + 1
            #updates max_value to keep track of the highest value of consonant substrings 
            # encountered during the iteration through the string.
            max_value = max(max_value, cons_value)
        else:
            cons_value = 0   

    print(result) 
    print(max_value)       
conson()    