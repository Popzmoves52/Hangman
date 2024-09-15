import random
from hangman_words import word_list
from hangman_art import hangman
from hangman_art import logo

placeholder=""
lives=6
print(logo)
list=[]
random_word=random.choice(word_list)  #chooses the random word from the word_list
print(random_word) 
for y in random_word: #iterate the random word
    placeholder=placeholder+"_"
print(placeholder)
game_over=False


while not game_over: 
    display=""   
    user=input("guess the letter:").lower() #camel #c -user input
    if user in list:
         print("you have already guessed this letter ",user,"kindly try with any other letter.")
    else:     
        for x in random_word: #first letter x=c
            if x==user: #
                display+=x
                list.append(x)
                print(hangman[6])
            elif x in list:
                display+=x       
            else:
                display+="_"
        print(display)     
        if user not in random_word:
            lives=lives-1
            print(hangman[lives]) 
            print(f"You guess {user},that is not in the word.You loose a life.")   
            print("*******************",lives,"/6 LIVES LEFT*******************")
        if lives==0:
            print(f"--------------------IT WAS {random_word}!You loose--------------------")
            print("Its ok,loosing is the part of the game,RESTART and TRY AGAIN!") 
            game_over=True         
        if "_" not in display :
            game_over=True
            
            print("--------------------You are genius!You won--------------------")               
          





 




    



      


    
