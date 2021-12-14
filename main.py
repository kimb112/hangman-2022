# import random library


# import string module


# import words file


# validate words

  # randomly choose a word from the list
   
  
  # check if a word contains a hypen or space
   
    

  

# hangman function

  # computer chooses a word
  

  # store the correct user guesses
  

  # set of all letters the user can guess
  
  
  # store all user guesses
  

  # number of lives
  

  # while the length of the word is greater than 0 and the number of lives is greater than 0
  
    
    # print letters used
    #" ".join(["a", "b", "cd"]) -> 'a b cd'
    

    # print the current word
    
    

    # get user input
    

    # if the letter hasn't been used before
    
      # add the letter to the used-letters category
      
      
      # if the letter is in the word
      
        # remove the letter from the word
        

      # subtract one life if the letter is wrong
      
        
        
    
    # if the user guesses the same letter
    
      

    # if the user inputs a character that is not a letter
    
      

  # if there are no more lives left
  
    
  

    
# call the hangman function
