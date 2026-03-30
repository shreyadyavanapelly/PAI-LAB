import heapq


GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance



def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors




def is_solvable(state):
    flat = [num for row in state for num in row if num != 0]
    inversions = 0
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    return inversions % 2 == 0



def solve_puzzle(start_state):
    
    if not is_solvable(start_state):
        print("This puzzle is NOT solvable.")
        return None

    pq = []
    heapq.heappush(pq, (0 + manhattan_distance(start_state), 0, start_state, []))
    
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current in visited:
            continue
        
        visited.add(current)
        path = path + [current]

        if current == GOAL_STATE:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path))

    return None



def print_puzzle(state):
    for row in state:
        print(row)
    print()



start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))

solution = solve_puzzle(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves\n")
    for step in solution:
        print_puzzle(step)
