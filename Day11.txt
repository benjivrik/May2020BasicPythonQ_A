# ---------------------------------------------------
# Author    :  Benjamin Kataliko Viranga
# Community :  Stunt Business
# Community website : www.stuntbusiness.com
#
# 30 Days - Q&A Python Basic
# Day 11 : 1-06-2020
# Day 11 | IG : https://www.instagram.com/benjivrik/
# Subject : Challenge V - Rock Paper Scissor
#----------------------------------------------------
# what would be the output of this program ?

'''

    Rock Paper Scissor 

    Play Rock Paper Scissor with your computer

    Plays

    Player 1      Player 2       Winner
     Rock         Scissor       Player 1
     Rock          Rock         Equality
     Rock          Paper        Player 2
     Paper        Scissor       Player 2
     Paper         Rock         Player 1
     Paper         Paper        Equality
     Scissor      Scissor       Equality
     Scissor       Rock         Player 1
     Scissor       Paper        Equality   

'''

import random


#main program
available_plays =  ['Rock', 'Paper', 'Scissors']

#initialize score
user_score = 0
computer_score = 0
number_of_games = 0

stop = "no"
while stop == "no":

  print("\n------ Starting a new game of Rock Paper Scissors. ------\n")
  #computer play
  computer_play_index = random.randint(0, len(available_plays)-1)
  computer_play =  available_plays[computer_play_index]
  #request user play
  user_play = input("Please choose between 'Rock', 'Paper' or 'Scissors':")
  while not user_play in available_plays :
    user_play = input("Please enter your choice, as written, between 'Rock', 'Paper' or 'Scissors':")

  #number of games
  number_of_games =  number_of_games + 1

  print('\n')
  
  if(computer_play == 'Rock') :

    if(user_play == 'Rock') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> We are equal here. Let's continue <\n")

    if(user_play == 'Paper') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> You win. <\n")
      user_score = user_score + 1 #increment user_score

    if(user_play == 'Scissors') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> I win. <\n")
      computer_score = computer_score + 1

  if (computer_play == 'Paper') :

    if(user_play == 'Paper') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> We are equal here. Let's continue <\n")

    if(user_play == 'Scissors') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> You win. <\n")
      user_score = user_score + 1 #increment user_score

    if(user_play == 'Rock') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> I win. <\n")
      computer_score = computer_score + 1

  if (computer_play == 'Scissors'):

    if(user_play == 'Scissors') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> We are equal here. Let's continue <\n")

    if(user_play == 'Rock') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> You win. <\n")
      user_score = user_score + 1 #increment user_score

    if(user_play == 'Paper') :
      print("I played : {}.\nAnd you played {}.".format(computer_play,user_play))
      print("\n> I win. <\n")
      computer_score = computer_score + 1

  #stats
  print('\n --- Current Stats. ---')
  print('> User score :{}'.format(user_score))
  print('> Computer score : {}'.format(computer_score))
  print('> Draws : {}'.format(number_of_games - (user_score+computer_score)))

  #ask the user if he wants to contine
  stop = input("\nDo you wanna stop ? yes or no : ")

  if(stop != "yes"):
      stop = "no"
  else :

      print('\n--- Final Stats. ---')
      print('> Number of games :{}'.format(number_of_games))
      print('> User score :{}'.format(user_score))
      print('> Computer score : {}'.format(computer_score))
      print('> Draws : {}'.format(number_of_games - (user_score+computer_score)))

      break #stop the loop 

print("End of program.")