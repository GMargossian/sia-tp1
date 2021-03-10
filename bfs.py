import copy

from common import finished, next_configs, process_results
from utils import *

ALGORITHM_NAME = "Breadth First Search (BFS)"

# def unordered_positions_equal(list1, list2):
#     still_equal = True
#     for (i, j) in list1:
#         still_equal = False
#         for (k, l) in list2:
#             if (i == k and j == l):
#                 still_equal = True
#         if not still_equal:
#             return False

#     return True
        
# def config_was_used(config, processed):
    # for cfg in processed:
    #     if cfg['player'][0] == config['player'][0] and cfg['player'][1] == config['player'][1] and unordered_positions_equal(cfg['boxes'], config['boxes']):
    #         return True
    # return False
    # return config in processed

def build_path(node):
    path = []

    n = copy.copy(node)

    while n.father != None:
        path.insert(0, n.config)
        n = n.father

    path.insert(0, n.config)

    return path
            
def bfs(level):
    smap = level.smap

    first_node = Node(level.start, None, [])

    queue = []

    #metemos al nodo inicial en la cola

    queue.append(first_node)
    processed = set()

    nodes_processed = 0

    # mientras que la cola tenga elementos y no gane

    won = False

    while queue and not won:
        
        # saco el primer nodo de la cola
        node = queue.pop(0)
        # print("Current node: ", node.config)

        # agrego este nodo a los nodos procesados
        processed.add(node.config)

        # primero me fijo si gane
        if(finished(node.config.boxes, level)):
            # si gane listo
            print("Found solution!")
            won = True
            
        else:
            nodes_processed += 1

            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node.config, level.smap)
            # print("Possible configs: ", possible_configs)

            children = node.children
            
            #por cada movimiento legal me fijo si ya tube esta config antes y si no la apendeo a la cola
            
            for config in possible_configs.difference(processed):
                new_node = Node(copy.copy(config), node, [])
                children.append(new_node)
                queue.append(new_node)
                # print("Added move: ", new_node.config)

            # print("Used configs: ", processed)
            # print("Queue is: ", queue)

    if won:
        path = build_path(node)
        return process_results(won, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, len(queue))
    else:
        return process_results(won, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, len(queue))

