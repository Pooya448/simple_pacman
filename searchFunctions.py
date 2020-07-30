import util
from game import Directions

UNREACHABLE_GOAL_STATE = [Directions.STOP]


def tinyMazeSearch(problem):
    """
    Run to get familiar with directions.
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    Run this function to get familiar with how navigations works using Directions enum.
    """

    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH
    to_goal_easy_directions = [s, s, w, s, w, w, s, w]
    return to_goal_easy_directions


def simpleMazeSearch(problem):
    """
    Q1:
    Search for the goal using right-hand or left-hand method explained in docs.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getNextStates(problem.getStartState())
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"

    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    right_hand = {n: e, w: n, s: w, e: s}
    left_hand = {n: w, w: s, s: e, e: n}
    ass = {n: s, w: e, s: n, e: w}

    currentNode = problem.getStartState()
    actions = []
    direction = Directions.NORTH
    while not problem.isGoalState(currentNode):
        flag = True
        nexts = problem.getNextStates(currentNode)
        for state, action, _ in nexts:
            if right_hand[direction] == action:
                actions += [action]
                currentNode = state
                direction = action
                flag = False
                break
        if flag:
            for state, action, _ in nexts:
                if direction == action:
                    actions += [action]
                    currentNode = state
                    direction = action
                    flag = False
                    break
        if flag:
            for state, action, _ in nexts:
                if left_hand[direction] == action:
                    actions += [action]
                    currentNode = state
                    direction = action
                    flag = False
                    break
        if flag:
            for state, action, _ in nexts:
                if ass[direction] == action:
                    actions += [action]
                    currentNode = state
                    direction = action
                    break

    return actions

    "*** YOUR EXPLANATION HERE***"
    """
        Yes, beacause eventually pacman reaches the exit point (the goal) in this way, because always the goal can be reached through edges of the walls
        If the goal is unreachable, this algorithms just loops over and over and fails
    """


def dfs(problem):
    """
    Q2:
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal.
    Make sure to implement a graph search algorithm.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    visited = []
    nodeStack = util.Stack()
    startNode = problem.getStartState()
    nodeStack.push((startNode, []))
    while nodeStack.isEmpty() == False:
        node, action = nodeStack.pop()
        if visited.__contains__(node):
            continue
        if problem.isGoalState(node):
            return action
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            nodeStack.push((n, action + [a]))

    return Directions.STOP
    "*** YOUR EXPLANATION HERE***"
    """
        No, pacman doesn't examin all houses, and the reason is OBVIOUS
    """


def bfs(problem):
    """
    Q3:
    Search the shallowest nodes in the search tree first.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    visited = []
    nodeQueue = util.Queue()
    startNode = problem.getStartState()
    nodeQueue.push((startNode,[]))
    while nodeQueue.isEmpty() == False:
        node, action = nodeQueue.pop()
        if visited.__contains__(node):
            continue
        if problem.isGoalState(node):
            return action
        visited.append(node)
        successors = problem.getNextStates(node)
        for n, a, c in successors:
            nodeQueue.push((n,action + [a]))
    "*** YOUR EXPLANATION HERE***"
    """
        BFS algorithm expands nodes layer by layer, so in a graph without weights, bfs always finds the shortest path because of the layer by layer searching mechanism
    """

def find_dead(problem, founds, startNode):

    visited = []
    nodeQueue = util.Queue()
    nodeQueue.push((startNode,[]))
    while not nodeQueue.isEmpty():
        node, action = nodeQueue.pop()
        if visited.__contains__(node):
            continue
        if is_deadend(problem,node,founds):
            founds += [node]
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            nodeQueue.push((n,action + [a]))
    return True

def find_first_dead(problem, founds, startNode):

    visited = []
    nodeQueue = util.Queue()
    nodeQueue.push((startNode,[]))
    while not nodeQueue.isEmpty():
        node, action = nodeQueue.pop()
        if visited.__contains__(node):
            continue
        if is_deadend(problem,node,founds):
            founds += [node]
            return action
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            nodeQueue.push((n,action + [a]))
    return None

def find_path(problem, start_node, end_node):

    visited = []
    nodeQueue = util.Queue()
    startNode = start_node
    nodeQueue.push((startNode,[]))
    while nodeQueue.isEmpty() == False:
        node, action = nodeQueue.pop()
        if visited.__contains__(node):
            continue
        if node == end_node:
            return action
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            nodeQueue.push((n,action + [a]))

def find_path_to_goal(problem, start_node):

    visited = []
    nodeQueue = util.Queue()
    startNode = start_node
    nodeQueue.push((startNode,[]))
    while nodeQueue.isEmpty() == False:
        node, action = nodeQueue.pop()
        if visited.__contains__(node):
            continue
        if problem.isGoalState(node):
            return action
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            nodeQueue.push((n,action + [a]))
def deadend(problem):
    """
    Q5: Search for all dead-ends and then go for goal state.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    founds = []
    founds.append(problem.getStartState())
    path = []


    # flag = True
    # while flag:
    #     action = find_first_dead(problem,founds,founds[len(founds) - 1])
    #     if action == None:
    #         break
    #     path += action
    #
    # path += find_path_to_goal(problem, founds[len(founds) - 1])

    find_dead(problem,founds,problem.getStartState())
    r = len(founds)

    for i in range(r - 1):
        path += find_path(problem, founds[i], founds[i + 1])

    path += find_path_to_goal(problem, founds[r - 1])

    return path



def ucs(problem):
    """
    Q7: Search the node of least total cost first.
    Dont forget to take a look at handy classes implemented in util.py.
    """

    "*** YOUR CODE HERE ***"
    visited = []
    pQueue = util.PriorityQueue()
    startNode = problem.getStartState()
    pQueue.push((startNode, []), 0)
    while pQueue.isEmpty() == False:
        node, action = pQueue.pop()
        if visited.__contains__(node):
            continue
        if problem.isGoalState(node):
            return action
        visited.append(node)
        for n, a, c in problem.getNextStates(node):
            pQueue.push((n, action + [a]), c)
    "*** YOUR EXPLANATION HERE***"
    """
        BFS is a special case of UCS, Imagine if all costs are same (.i.e 1), BFS and UCS are exactly the same
    """

def is_deadend(problem, node, visited):
    if len(problem.getNextStates(node)) == 1 and not node in visited:
        return True
    return False