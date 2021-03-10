import copy

from utils import *
import constants
import visual

def finished(boxes, level):
    return boxes == level.goals

cornering_directions = [
    [
        [-1, 0],
        [0, -1]
    ],
    [
        [-1, 0],
        [0, 1]
    ],
    [
        [1, 0],
        [0, -1]
    ],
    [
        [1, 0],
        [0, 1]
    ],
]


directions = [
    [-1, 0], #arriba
    [0, -1], #izquierda
    [1, 0], #abajo
    [0, 1] #derecha
]


def box_becomes_immovable(box, smap):

    global cornering_directions

    for ((i, j), (k, l)) in cornering_directions:
        pos1 = [box[0] + i, box[1] + j]
        pos2 = [box[0] + k, box[1] + l]

        if(smap[pos1[0], pos1[1]] == constants.WALL and smap[pos2[0], pos2[1]] == constants.WALL):
            return True

    return False

def next_configs(config, smap):
    player = config.player
    boxes = config.boxes

    smap_wb = smap.copy()

    #create an auxiliar map with box information for faster checks
    for pos in boxes:
        smap_wb[pos.x, pos.y] = constants.BOX

    configs = set()

    global directions

    #por cada una de las 4 direcciones
    for (i, j) in directions:
        #si tengo pared no puedo
        new_pos = Position(player.x + i, player.y + j)
        
        if smap_wb[new_pos.x, new_pos.y] != constants.WALL:
            #si hay una caja
            if smap_wb[new_pos.x, new_pos.y] == constants.BOX:
                #tengo que fijarme si una mas en la misma direccion hay o una pared o una caja
                if smap_wb[player.x + 2*i, player.y + 2*j] != constants.WALL and smap_wb[player.x + 2*i, player.y + 2*j] != constants.BOX and (not box_becomes_immovable([player.x + 2*i, player.y + 2*j], smap) or smap_wb[player.x + 2*i, player.y + 2*j] == constants.GOAL):
                    # me fijo si la caja que movi quedo en una posicion inganable, de ser asi no se mete el caso

                    new_box_pos = Position(player.x + 2*i, player.y + 2*j)
                    
                    for i in range(0, len(new_boxes)):
                        if new_boxes[i] == new_pos:
                            new_boxes[i] = new_box_pos

                    # print("Box Moving Config --> ", Config(new_pos, new_boxes))

                    # me muevo a mi y a la caja
                    configs.add(Config(new_pos, set(new_boxes)))                    
            #no hay una caja (hay un espacio vacio)
            else:
                # print("No Box Moving Config --> ", Config(new_pos, copy.deepcopy(boxes)))
                configs.add(Config(new_pos, copy.deepcopy(boxes)))

    return configs

def process_results(success, smap, node, path, alg, proc_nodes_amt, front_nodes_amt):
    for move in path:
        simple_printing(smap, move)

    if success:
        success_text = 'Success'
    else:
        success_text = 'Failure' 
    
    results = {
        'algorithm': alg,
        'result': success,
        'depth': len(path) - 1,
        'cost': "Not implemented yet",
        'nodes expanded': proc_nodes_amt,
        'frontier nodes': front_nodes_amt,
        'solution': path
    }
    
    print('Algorithm: ', alg)
    print('Result: ', success_text)
    print('Depth: ',  len(path) - 1)
    print('Cost: ', "Not implemented yet")
    print('Nodes expanded: ', proc_nodes_amt)
    print('Frontier nodes: ', front_nodes_amt)
    print('Solution: ', path)

    if success:
        visual.play(smap, path)

    return results
                 

def simple_printing(smap, positions):

    smap_wbp = smap.copy()

    for i in range(0, len(smap_wbp)):
        smap_wbp[i] = smap_wbp[i].copy()
        
    print(positions)
    
    print("frozen: ", frozenset(positions.boxes))

    #create an auxiliar map with box information for faster checks
    for box in positions.boxes:
        smap_wbp[box.x, box.y] = constants.BOX

    player = positions.player

    smap_wbp[player.x, player.y] = constants.PLAYER

    print('---------------------------------------------')

    print(smap_wbp)
    
    print('---------------------------------------------')