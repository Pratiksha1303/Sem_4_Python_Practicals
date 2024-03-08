# Make a two-player Rock-Paper-Scissors game

#(Hint: Ask for player plays (using input), compare them, print out a meassage of congratulations to the winner, ask if the players want to start a new game)

# Remember the rules: Rock beats scissors, Scissors beat paper, Paper beats rock

def game():
   ch = 'y'
   while(ch == 'y'):
       u1 = input('what do you choose user1:')
       u2 = input('what do you choose user2:')

       if(u1 == u2):
            print("Tie game")
    
       elif(u1 == 'rock'):
            if(u2 == 'paper'):
                print("u2, paper wins")
            else:
                print("u1, rock wins")
       elif(u1 == 'paper'):
            if(u2 == 'scissors'):
                print("u2, scissor wins")
            else:
                print("u1, paper wins")
       elif(u1 == 'scissors'):
             if(u2 == 'rock'):
                print("u2, rock wins")
             else:
                print("user1, scissor wins")
       ch = input('Do you want to play a game? y/n :')
game()


#   what do you choose user1:paper
#   what do you choose user2:rock
#   u1, paper wins
#   Do you want to play a game? y/n :y
#   what do you choose user1:rock
#   what do you choose user2:scissors
#   u1, rock wins
#   Do you want to play a game? y/n :y
#   what do you choose user1:scissors
#   what do you choose user2:paper
#   user1, scissor wins
#   Do you want to play a game? y/n :n