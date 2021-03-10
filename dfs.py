import copy

from common import finished, next_configs, process_results
from utils import *

ALGORITHM_NAME = "Depth First Search (DFS)"


def build_path(node):
    path = []

    n = copy.copy(node)

    while n.father != None:
        path.insert(0, n.config)
        n = n.father

    path.insert(0, n.config)

    return path
            
def dfs(level):
    smap = level.smap

    first_node = Node(level.start, None, [])

    stack = []

    #metemos al nodo inicial en la cola

    stack.append(first_node)
    processed = set()

    nodes_processed = 0

    # mientras que la cola tenga elementos y no gane

    won = False

    while stack and not won:
        
        # saco el primer nodo del stack
        node = stack.pop()
        # print('ITERATION: ', nodes_processed, ' --------------------------------------------------------------')
        # print("Current node: ", node.config)

        # agrego este nodo a los nodos procesados
        processed.add(node.config)
    
        # primero me fijo si gane
        if(finished(node.config.boxes, level)):
            # si gane listo
            # print("Found solution!")
            won = True
        else:
            nodes_processed += 1

            # si no gane pido mis movimientos legales
            possible_configs = next_configs(node.config, level.smap)
            # print("Possible configs: ", possible_configs)

            children = node.children
            
            #por cada movimiento legal me fijo si ya tube esta config antes y si no la apendeo a la cola
            # print("Procesed: ===>", processed)
            for config in possible_configs.difference(processed):
                # print("Config: +++>", config)
                # print("Was not in processed")
                new_node = Node(copy.copy(config), node, [])
                children.append(new_node)
                stack.append(new_node)
                # print("Added move: ", new_node.config)

            # print("Used configs: ", processed)
            # print("Stack is: ", stack)

    if won:
        path = build_path(node)
        return process_results(won, smap, node, path, ALGORITHM_NAME, nodes_processed - 1, len(stack))
    else:
        return process_results(won, smap, None, [], ALGORITHM_NAME, nodes_processed - 1, len(stack))

