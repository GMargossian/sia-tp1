import copy

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # print("comparing: ", self, " with ", other, " will return ", self.x == other.x and self.y == other.y)
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        # print("hashing pos: ", self)
        return hash((self.x, self.y))

    def __sortkey__(self):
        return hash((self.x, self.y))

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)


class Config:
    def __init__(self, player, boxes):
        self.player = player
        self.boxes = boxes

    def __eq__(self, other):
        # print("comparing: ", self, " with ", other, " will return ", self.player == other.player and self.boxes == other.boxes)
        return self.player == other.player and self.boxes == other.boxes
    def __hash__(self):    
        # print("hashing cfg: ", self)
        return hash((self.player, frozenset(self.boxes)))

    def __sortkey__(self):
        return hash((self.x, self.y))
    
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result
    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, copy.deepcopy(v, memo))
        return result

    def __str__(self):
        return "<Player: %s, Boxes: %s>" % (str(self.player), str(self.boxes))
    def __repr__(self):
        return "<Player: %s, Boxes: %s>" % (str(self.player), str(self.boxes))


class Node:
    def __init__(self, config, father, children, depth = None):
        self.config = config
        self.father = father
        self.children = children
        self.depth = depth
    

class Level:
    def __init__(self, name, start, smap, goals):
        self.name = name
        self.start = start
        self.smap = smap
        self.goals = goals