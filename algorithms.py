import bfs, dfs, iddfs

def BFS(level):
    print('BFS')
    return bfs.bfs(level)

def DFS(level):
    print('DFS')
    return dfs.dfs(level)

def IDDFS(level):
    print('IDDFS')
    return iddfs.iddfs(level)

def GGS(level):
	print('GGS')

def AStar(level):
	print('AStar')

def IDAStar(level):
	print('IDAStar')

algorithms = [
    {
        "name": bfs.ALGORITHM_NAME,
        "func": BFS,
    },
    {
        "name": dfs.ALGORITHM_NAME,
        "func": DFS,
    },
    {
        "name": "Iterative Deepening Depth First Search (IDDFS)",
        "func": IDDFS,
    },
    {
        "name": "GGS",
        "func": GGS,
    },
    {
        "name": "AStar",
        "func": AStar,
    },
    {
        "name": "IDAStar",
        "func": IDAStar,
    },
]