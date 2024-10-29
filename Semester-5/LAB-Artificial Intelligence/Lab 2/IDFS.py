from copy import deepcopy

def IDFS(initial_state, goal_state):
    for depth in range(1, 100):  
        visited = [initial_state]
        result = IDDFS(initial_state, goal_state, visited, depth)
        if result is not None:
            return result
    return None

def IDDFS(initial_state, goal_state, visited, depth):
    if initial_state == goal_state:
        return initial_state
    if depth <= 0:
        return None

    ind = index_empty(initial_state)
    i = ind[0]
    j = ind[1]

    for pos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        li = deepcopy(initial_state)
        new_pos = (i + pos[0], j + pos[1])

        if 0 <= new_pos[0] <= 2 and 0 <= new_pos[1] <= 2:
            li[i][j] = li[new_pos[0]][new_pos[1]]
            li[new_pos[0]][new_pos[1]] = 0

            if li not in visited:
                visited.append(li)
                result = IDDFS(li, goal_state, visited, depth - 1)
                if result is not None:
                    return result

    return None

def display_puzzle(li):
    count = 0
    for i in li:
        if count == 3:
            count = 0
            print()
            print()

        print(i)
        count += 1

def index_empty(li):
    for i in range(len(li)):
        for j in range(3):
            if li[i][j] == 0:
                return (i, j)

def main():
    initial_state = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    result = IDFS(initial_state, goal_state)

    if result is not None:
        print("Solution found:")
        display_puzzle(result)
    else:
        print("No solution found")

main()