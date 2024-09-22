cells = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1
while True:
# draw table
    print(f' {cells[0]}  |  {cells[1]} |  {cells[2]} ')
    print('____|____|____')
    print(f' {cells[3]}  |  {cells[4]} |  {cells[5]} ')
    print('____|____|____')
    print(f' {cells[6]}  |  {cells[7]} |  {cells[8]} ')
    print('    |    |    ')

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


    if cells[0]==cells[4] and cells[4]==cells[8]:
        print(f"{player} has won")
        break
    if cells[0]==cells[4] and cells[4]==cells[8]:
        print(f"{player} has won")
        break