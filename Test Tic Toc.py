game_board={'1':'','2':'','3':'', 
'4':'', '5':'','6':'',
'7':'','8':'','9':''}

board_keys=[]
for key in game_board:
    board_keys.append(key)



def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('--')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('--')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game_play():
    turn='X'
    count=0

    for i in range (10):
        print_board(game_board)
        print('Its Your Turn \n'  + turn + ' Select Your Place')

        move=input()

        if game_board[move] == '' :
            game_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ': # across the top
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ': # across the middle
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ': # across the bottom
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ': # down the left side
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ': # down the middle
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ': # down the right side
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ': # diagonal
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ': # diagonal
                print_board(game_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break         

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")



        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'



    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            game_board[key] = " "
        game_play()


if __name__ == "__main__":
    game_play()                   
    