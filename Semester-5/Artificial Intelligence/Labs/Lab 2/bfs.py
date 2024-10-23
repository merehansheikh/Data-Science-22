from collections import deque
from copy import deepcopy

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [initial_state])])
    visited = set(tuple(map(tuple, initial_state)))

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            print("Solution Found")
            return path

        ind = index_empty(state)
        i = ind[0]
        j = ind[1]

        for pos in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_state = deepcopy(state)
            new_pos = (i + pos[0], j + pos[1])

            if 0 <= new_pos[0] <= 2 and 0 <= new_pos[1] <= 2:
                new_state[i][j], new_state[new_pos[0]][new_pos[1]] = new_state[new_pos[0]][new_pos[1]], new_state[i][j]

                if tuple(map(tuple, new_state)) not in visited:
                    visited.add(tuple(map(tuple, new_state)))
                    queue.append((new_state, path + [new_state]))

    print("No Solution exist")
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
    v = bfs(initial_state, goal_state)
    if v:
        for state in v:
            display_puzzle(state)
            print()


main()