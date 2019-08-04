def feltcher(codigo):
    codigo1= 0
    codigo2 = 0
    
    for i in codigo:
        codigo1 += i
        codigo2 += codigo1
    codigo1 = c1%255
    codigo2 = c2%255
    
    return codigo1, codigo2