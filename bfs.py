import rubik
import pickle

def BFS(s):
    # stores the level of a state (number of moves from solved state)
    level = {s: 0}
    # stores the parent of a state (previous state)
    parent = {s: None}
    
    i = 1

    # current layer of BFS
    frontier = [s]
    
    while frontier:
        print(len(frontier))   
        n = []  #n stands for next
        
        # iterate through all the frontiers
        for u in frontier:
            #iterate through all possible moves
            for move in rubik.moves:    
                v = rubik.apply_move(move, u)
                # check if state has already been visited earlier
                if v not in level:      
                    level[v] = i
                    parent[v] = u
                    n.append(v)
                else:
                    u = rubik.apply_move(rubik.invert_move(move), v)

        frontier = n
        i+=1

    # save level dictionary and parent dictionary to not redo BFS each time
    levelFile = open("level.pkl","wb")
    parentFile = open("parent.pkl","wb")
    
    pickle.dump(level, levelFile)
    pickle.dump(parent, parentFile)
    
    levelFile.close()
    parentFile.close()    
    

BFS(rubik.I)
