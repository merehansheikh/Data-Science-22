import heapq

class Node:
    def __init__(self, state, parent, move, h_cost):
        self.state = state          # Puzzle configuration (list of numbers)
        self.parent = parent        # Reference to the parent node
        self.move = move            # Move that led to this state (up, down, left, right)
        self.h_cost = h_cost        # Heuristic cost (Manhattan distance)
    
    # For priority queue (heapq), nodes will be compared by h_cost
    def __lt__(self, other):
        return self.h_cost < other.h_cost

# Calculate the Manhattan Distance for the current state
def calculate_heuristic(state, goal_state):
    h_cost = 0
    for i in range(1, 9):  # Ignore the 0 tile (empty space)
        x1, y1 = divmod(state.index(i), 3)  # Current position
        x2, y2 = divmod(goal_state.index(i), 3)  # Goal position
        h_cost += abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
    return h_cost

# Generate possible moves (children) from the current state
def generate_children(node, goal_state):
    children = []
    moves = ['up', 'down', 'left', 'right']
    x, y = divmod(node.state.index(0), 3)  # Get the position of the empty space (0)
    
    # Possible moves based on the empty space's position
    move_positions = {'up': (x - 1, y), 'down': (x + 1, y), 'left': (x, y - 1), 'right': (x, y + 1)}
    
    for move in moves:
        new_x, new_y = move_positions[move]
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check if the move is within bounds
            new_state = node.state[:]  # Copy current state
            new_index = new_x * 3 + new_y  # Get the index of the new empty space
            # Swap the 0 with the new position
            new_state[node.state.index(0)], new_state[new_index] = new_state[new_index], new_state[node.state.index(0)]
            # Create a new node (child)
            new_h_cost = calculate_heuristic(new_state, goal_state)
            child = Node(new_state, node, move, new_h_cost)
            children.append(child)
    
    return children

# Greedy Best-First Search algorithm
def GBFS(start_state, goal_state):
    # Priority queue to store nodes to be expanded, sorted by heuristic cost (h_cost)
    open_list = []
    # Add the starting node to the priority queue
    start_node = Node(start_state, None, None, calculate_heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)
    closed_list = set()  # Set to track visited states

    while open_list:
        current_node = heapq.heappop(open_list)  # Get the node with the smallest h_cost

        if current_node.state == goal_state:  # Goal reached
            return trace_solution(current_node)
        
        closed_list.add(tuple(current_node.state))  # Mark the current state as visited
        
        # Generate children (possible moves) and add them to the priority queue
        for child in generate_children(current_node, goal_state):
            if tuple(child.state) not in closed_list:
                heapq.heappush(open_list, child)

    return None  # No solution found

# Trace the solution path from goal to start
def trace_solution(node):
    path = []
    while node.parent:
        path.append(node.move)
        node = node.parent
    path.reverse()  # Reverse the path to get the moves from start to goal
    return path

# Example usage
start_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]  # Start configuration
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]   # Goal configuration

solution = GBFS(start_state, goal_state)
if solution:
    print("Solution found! Moves:", solution)
else:
    print("No solution exists.")
