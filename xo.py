cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1
def displayTable():
    print(f' {cells[0]}  |  {cells[1]} |  {cells[2]} ')
    print('____|____|____')
    print(f' {cells[3]}  |  {cells[4]} |  {cells[5]} ')
    print('____|____|____')
    print(f' {cells[6]}  |  {cells[7]} |  {cells[8]} ')
    print('    |    |    ')

def checkWinner(a, b, c, player):
    if a==b and b==c:
        print(f"{player} has won")
        return True
while True:
# draw table
    displayTable()

    player = "x"
    if turn%2 == 0 :
        player = "O"
    player_input = input("choose a cell : ")
    i = 0
    while i < len(cells):
        if player_input == cells[i] :
            cells[i] = player
        i += 1
    turn += 1


    if checkWinner(cells[0], cells[1], cells[2], player) or checkWinner(cells[3], cells[4], cells[5], player):
        break