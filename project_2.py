import random

def blackjack ():
    number_of_cards = 52
    player_1 = [random.randrange(1,11) for i in range(number_of_cards)]
    player_2 = [random.randrange(1,11) for i in range(number_of_cards)]
    table = []

    print('Player 1 = ',player_1,'\nPlayer 2 =',player_2)

    play_card(player_1,player_2,table)
   

def play_card(player_1,player_2,table):
    player_1_move = False
    player_2_move = False   

    start_player = [0,1]
    choosen_player = random.choice(start_player)
    if choosen_player == 0: 
        player_1_move = True
    else:
        player_2_move = True
        print(choosen_player)

    while sum(table) != 21:
        print('\nSoma da mesa', sum(table),'\n')
        while player_1_move is True:
            choosen_card = random.choice(player_1) 
            table.append(choosen_card)
            player_1_move = False
            player_2_move = True    
            print('Player 1:',choosen_card,table,)
        while player_2_move is True: 
            choosen_card = random.choice(player_2)  
            table.append(choosen_card)
            player_1_move = True
            player_2_move = False
            print('Player 2: ',choosen_card,table)
        while sum(table) > 21:
            table.clear()
    if sum(table) == 21:
        print('\nSoma da mesa = ',sum(table),'Blackjack!!!!!!', 'Player 1 Ganhou!' if player_1_move == False else 'Player 2 Ganhou!')
        
                    

blackjack()
#print(random.choice(start_player) == start_player[0],random.choice(start_player) == start_player[1])