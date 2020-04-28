import rubik
import pickle

# load level and parent dictionaries required to determine solution
parentFile = open('parent.pkl', 'rb')
levelFile = open('level.pkl', 'rb')

parent = pickle.load(parentFile)
level = pickle.load(levelFile)

# scrambled state taken from rubik.py file
scrambled = rubik.input_configuration()

# level[scrmabled] steps required to solve
for i in range(level[scrambled]):
    # get parent of current scarmbled state
    scrambled_parent = parent[scrambled]
    
    if scrambled_parent == rubik.apply_move(rubik.F, scrambled):
        scrambled = rubik.apply_move(rubik.F, scrambled)
        print('F')
    elif scrambled_parent == rubik.apply_move(rubik.Fi, scrambled):
        scrambled = rubik.apply_move(rubik.Fi, scrambled)
        print('Fi')
    elif scrambled_parent == rubik.apply_move(rubik.F2, scrambled):
        scrambled = rubik.apply_move(rubik.F2, scrambled)
        print('F2')
    elif scrambled_parent == rubik.apply_move(rubik.U, scrambled):
        scrambled = rubik.apply_move(rubik.U, scrambled)
        print('U')
    elif scrambled_parent == rubik.apply_move(rubik.Ui, scrambled):
        scrambled = rubik.apply_move(rubik.Ui, scrambled)
        print('Ui')
    elif scrambled_parent == rubik.apply_move(rubik.U2, scrambled):
        scrambled = rubik.apply_move(rubik.U2, scrambled)
        print('U2')
    elif scrambled_parent == rubik.apply_move(rubik.L, scrambled):
        scrambled = rubik.apply_move(rubik.L, scrambled)
        print('L')
    elif scrambled_parent == rubik.apply_move(rubik.Li, scrambled):
        scrambled = rubik.apply_move(rubik.Li, scrambled)
        print('Li')
    elif scrambled_parent == rubik.apply_move(rubik.L2, scrambled):
        scrambled = rubik.apply_move(rubik.L2, scrambled)
        print('L2')
