
win = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

# Player 1 == X
# Player 2 == O
OX = """

1 | 2 | 3
-----------
4 | 5 | 6
-----------
7 | 8 | 9

"""

X = []
O = []


class Duplicate(Exception):
    pass


def check_duplicate(position):
    duplicate = X + O
    
    if position in duplicate:
        raise Duplicate('Plase enter new position')


def check_draw():
    return (len(X) + len(O)) == 9

def check_win(p):
    for w in win:
        check = all(value in p for value in w)
        if check:
            return True
    return False


def displayOX(player_position=None, i=None):
    global OX
    syn = ''
    str_posi = str(player_position)
    if i == 1:
        syn = 'X'
    elif i == 2:
        syn = 'O'

    OX = OX.replace(str_posi, syn)    
    print(OX)
          

def play_game():
    i = 1
    while True:
        try:
            position = int(input(f'Player {i} enter posision[1-9] or 0(exit): '))
            if position > 9 or position < 0 :
                raise IndexError
            check_duplicate(position)
            
        except (ValueError, TypeError, IndexError):
            print('Please Enter Number[1-9] or exit.')
            displayOX()
            continue
        except Duplicate as err:
            print(err)
            displayOX()
            continue


        if position == 0:
            break

        if i == 1:
            X.append(position)
            displayOX(position, i)
            if check_win(X):
                print("Player X win!")
                break

            # Switch player
            i = 2
        elif i == 2:
            O.append(position)
            displayOX(position, i)
            if check_win(O):
                print("Player O win!")
                break

            # Switch player
            i = 1
        
        if check_draw():
            print("draw!")
            break


if __name__ == "__main__":
    displayOX()
    play_game()
