#!/usr/bin/env python
# coding: utf-8

# In[16]:


from IPython.display import clear_output
def display_board(board):
    print(f"{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}")
    print(f"{board[7]}|{board[8]}|{board[9]}")
test_board=["#","#","X","#","X","0","0","X","P","X"]
display_board(test_board)


# In[17]:


def player_input():
    maker=""
    while  not (maker=="X" or maker=="O"):
        maker=input("player1:choose X or O:").upper()
        
    if maker=="X":
        return('X','O')
    else:
        return('O','X')
     


# In[18]:


def place_maker(board, maker, position):
    board[position] = maker


# In[19]:


def wincheck(board,mark):
    
    return ((board[1]==board[2]==board[3]==mark)or 
    (board[4]==board[5]==board[6]==mark)or
    (board[7]==board[8]==board[9]==mark)or
    (board[1]==board[4]==board[7]==mark)or
    (board[2]==board[5]==board[8]==mark)or
    (board[3]==board[6]==board[9]==mark)or
    (board[1]==board[5]==board[9]==mark)or
    (board[3]==board[5]==board[7]==mark))


# In[20]:


import random  
def choose_first():
    if random.randint(0,1)==0:
        return 'Player2'
    else:
        return 'Player1'

    


# In[21]:


def space_check(board,position):
     return board[position]==' '


# In[22]:


def full_board_check(board):
    for i in range(1,10):
          if space_check(board,i):
                return False
    return True


# In[23]:


def player_choice(board):
    position =0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose  the postion (1,9):"))
        
    return position


# In[24]:


def replay():
    return input("play again?Enter yes or no :").lower().startwith('y')


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_maker, player2_maker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player1_maker, position)

            if wincheck(theBoard, player1_maker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player2_maker, position)

            if wincheck(theBoard, player2_maker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:





# In[ ]:




