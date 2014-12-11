barpos = 50
 
while True:
    move = input('What dirction"')
    if move == 'k':
        barpos = barpos-1
    if move == 'l':
        barpos = barpos+1
    print(move)
    print(barpos)

