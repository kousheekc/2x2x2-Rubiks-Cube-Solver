#solved state colors
rgw = flu = 0 
gwr = luf = 1 
wrg = ufl = 2 

rwb = fur = 3 
wbr = urf = 4 
brw = rfu = 5 

ryg = fdl = 6
ygr = dlf = 7
gry = lfd = 8 

rby = frd = 9
byr = rdf = 10 
yrb = dfr = 11

owg = bul = 12 
wgo = ulb = 13 
gow = lbu = 14 

obw = bru = 15
bwo = rub = 16 
wob = ubr = 17

ogy = bld = 18
gyo = ldb = 19
yog = dbl = 20

oyb = bdr = 21
ybo = drb = 22 
boy = rbd = 23

# apply a move to the current state
def apply_move(perm, position):
    return tuple([position[i] for i in perm])

# returns the inverse of a move
def invert_move(p):
    n = len(p)
    q = [0]*n
    for i in range(n):
        q[p[i]] = i
    return tuple(q)

# solved state
I = (flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr,
     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

# front face rotated clockwise
F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, 
     bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
# front face rotated counter-clockwise
Fi = invert_move(F)
# front face rotated twice
F2 = (frd, rdf, dfr, fdl, dlf, lfd, fur, urf, rfu, flu, luf, ufl,
      bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

# left face rotated clockwise
L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,
     dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
# left face rotated counter-clockwise
Li = invert_move(L)
# left face rotated twice
L2 = (bld, ldb, dbl, fur, urf, rfu, bul, ulb, lbu, frd, rdf, dfr,
      fdl, dlf, lfd, bru, rub, ubr, flu, luf, ufl, bdr, drb, rbd)

# upper face rotated clockwise
U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,
     luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
# upper face rotated counter-clockwise
Ui = invert_move(U)
# upper face rotated twice
U2 = (bru, rub, ubr, bul, ulb, lbu, fdl, dlf, lfd, frd, rdf, dfr,
      fur, urf, rfu, flu, luf, ufl, bld, ldb, dbl, bdr, drb, rbd)

moves = (F, Fi, F2, L, Li, L2, U, Ui, U2)

moves_names = {}
moves_names[F] = 'F'
moves_names[Fi] = 'Fi'
moves_names[F2] = 'F2'
moves_names[L] = 'L'
moves_names[Li] = 'Li'
moves_names[L2] = 'L2'
moves_names[U] = 'U'
moves_names[Ui] = 'Ui'
moves_names[U2] = 'U2'


def input_configuration():
    position = [-1]*24

    '''place cubie with yellow, blue, and orange faces (it has the
    Rubiks mark) in the lower-back-right corner with the yellow face down.'''

    front = [['r','r'],
             ['r','r']]

    back = [['o','o'],
            ['o','o']]

    up = [['w','w'],
          ['w','w']]

    down = [['y','y'],
            ['y','y']]

    left = [['g','g'],
            ['g','g']]

    right = [['b','b'],
             ['b','b']]

    position[0] = eval(front[0][0] + left[0][1] + up[1][0])
    position[1] = eval(left[0][1] + up[1][0] + front[0][0])
    position[2] = eval(up[1][0] + front[0][0] + left[0][1])
    
    position[3] = eval(front[0][1] + up[1][1] + right[0][0])
    position[4] = eval(up[1][1] + right[0][0] + front[0][1])
    position[5] = eval(right[0][0] + front[0][1] + up[1][1])
    
    position[6] = eval(front[1][0] + down[0][0] + left[1][1])
    position[7] = eval(down[0][0] + left[1][1] + front[1][0])
    position[8] = eval(left[1][1] + front[1][0] + down[0][0])
    
    position[9] = eval(front[1][1] + right[1][0] + down[0][1])
    position[10] = eval(right[1][0] + down[0][1] + front[1][1])
    position[11] = eval(down[0][1] + front[1][1] + right[1][0])
    
    position[12] = eval(back[0][1] + up[0][0] + left[0][0])
    position[13] = eval(up[0][0] + left[0][0] + back[0][1])
    position[14] = eval(left[0][0] + back[0][1] + up[0][0])
    
    position[15] = eval(back[0][0] + right[0][1] + up[0][1])
    position[16] = eval(right[0][1] + up[0][1] + back[0][0])
    position[17] = eval(up[0][1] + back[0][0] + right[0][1])
    
    position[18] = eval(back[1][1] + left[1][0] + down[1][0])
    position[19] = eval(left[1][0] + down[1][0] + back[1][1])
    position[20] = eval(down[1][0] + back[1][1] + left[1][0])
    
    position[21] = eval(back[1][0] + down[1][1] + right[1][1])
    position[22] = eval(down[1][1] + right[1][1] + back[1][0])
    position[23] = eval(right[1][1] + back[1][0] + down[1][1])
    
    return tuple(position)


