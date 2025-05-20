import sys  # Import the sys module to access system-specific parameters and functions
import time  # Add for performance timing
sys.setrecursionlimit(10**6)  # Set the recursion limit to prevent exceeding the maximum recursion depth

class ArrowNode:
    def __init__(self, x_position: int = -1, y_position: int = -1, color_direction_info: str = ''):
        # Initialize the ArrowNode with information about its position, color, and direction
        self.is_goal = False  # Flag to determine if the node represents the goal (bullseye)
        self.possible_next_arrows = []  # List to store potential next arrows along with their distances
        self.has_been_visited = False  # Flag to track whether the node has been visited during traversal
        self.x, self.y = x_position, y_position
        self.color, self.direction = (None, None) if color_direction_info == 'O' else color_direction_info.split('-')
        self.visited_in_path = False  # Track if visited in the solution path

    DIRECTION_STEPS = {
        'S': (1, 0),
        'N': (-1, 0),
        'W': (0, -1),
        'E': (0, 1),
        'SE': (1, 1),
        'NE': (-1, 1),
        'SW': (1, -1),
        'NW': (-1, -1)
    }

    def calculate_steps_to_next_arrow(self):
        # Determine the steps required to move in the specified arrow direction
        if self.direction in self.DIRECTION_STEPS:
            return self.DIRECTION_STEPS[self.direction]
        raise RuntimeError("Invalid arrow direction: " + str(self.direction) + " at coordinates: (" + str(self.x) + ", " + str(self.y) + ")")

    def identify_possible_next_arrow(self, another_arrow):
        # Identify the next arrow in the specified direction and calculate the distance
        if another_arrow.color != self.color:
            distance = max(abs(self.x - another_arrow.x), abs(self.y - another_arrow.y))
            self.possible_next_arrows.append((another_arrow, distance))

    def search_for_goal(self, result_path, path_coords=None, visited_nodes=None):
        # Conduct a depth-first search to locate the goal (bullseye) and record the path
        self.has_been_visited = True
        if visited_nodes is not None:
            visited_nodes.add((self.x, self.y))
        if path_coords is not None:
            path_coords.append((self.x, self.y))
        def insert_result(arrow_info):
            result_path.insert(0, f'{arrow_info[1]}{self.direction}')
        for next_arrow_info in self.possible_next_arrows:
            has_been_visited = next_arrow_info[0].has_been_visited
            direction_is_none = next_arrow_info[0].direction is None
            if not has_been_visited and direction_is_none:
                insert_result(next_arrow_info)
                if path_coords is not None:
                    path_coords.append((next_arrow_info[0].x, next_arrow_info[0].y))
                return True
            if not has_been_visited:
                found = next_arrow_info[0].search_for_goal(result_path, path_coords, visited_nodes)
                if found:
                    insert_result(next_arrow_info)
                    return found
        if path_coords is not None:
            path_coords.pop()
        return False

def visualize_maze(arrow_data_matrix, path_coords):
    # Print the maze with the solution path marked by '*' and colored output
    COLOR_RED = '\033[91m'
    COLOR_BLUE = '\033[94m'
    COLOR_GREEN = '\033[92m'
    COLOR_YELLOW = '\033[93m'
    COLOR_RESET = '\033[0m'
    path_set = set(path_coords)
    print("\nMaze with solution path (colored):")
    for i, row in enumerate(arrow_data_matrix):
        row_str = []
        for j, cell in enumerate(row):
            if (i, j) in path_set and cell != 'O':
                row_str.append(f"{COLOR_GREEN}*{COLOR_RESET}")
            elif cell == 'O':
                row_str.append(f"{COLOR_YELLOW}O{COLOR_RESET}")
            elif cell.startswith('R-'):
                row_str.append(f"{COLOR_RED}{cell}{COLOR_RESET}")
            elif cell.startswith('B-'):
                row_str.append(f"{COLOR_BLUE}{cell}{COLOR_RESET}")
            else:
                row_str.append(cell)
        print(' '.join(row_str))

def main_maze_solver(input_file, output_file):
    import copy
    with open(input_file, 'r') as file_handle:
        lines = file_handle.readlines()
        data = [line.split() for line in map(str.strip, lines)]
        row_count, col_count = map(int, data[0])
        arrow_data_matrix = data[1:len(data)]
    arrow_nodes = [ArrowNode(r, c, arrow_data_matrix[r][c]) for r in range(row_count) for c in range(col_count)]
    for idx in range(row_count * col_count):
        r_position, c_position = divmod(idx, col_count)
        arrow_node_instance = arrow_nodes[idx]
        try:
            r_step, c_step = arrow_node_instance.calculate_steps_to_next_arrow()
            while 0 <= r_position < row_count and 0 <= c_position < col_count:
                arrow_node_instance.identify_possible_next_arrow(arrow_nodes[r_position * col_count + c_position])
                r_position = r_position + r_step
                c_position = c_position + c_step
        except RuntimeError:
            pass
    result_goal_path = []
    path_coords = []
    visited_nodes = set()
    start_time = time.perf_counter()
    found = arrow_nodes[0].search_for_goal(result_path=result_goal_path, path_coords=path_coords, visited_nodes=visited_nodes)
    end_time = time.perf_counter()
    solution_goal_path = " ".join(result_goal_path) if found else None
    with open(output_file, 'w') as output_file_handle:
        output_file_handle.write(solution_goal_path if solution_goal_path is not None else "")
    # Visualize maze and print stats
    if found:
        visualize_maze(arrow_data_matrix, path_coords)
        print(f"\nPerformance stats:")
        print(f"Nodes visited: {len(visited_nodes)}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
    else:
        print("No solution found.")

if __name__ == "__main__":
# # Obtain input and output file names from command-line arguments
    input_file_name = sys.argv[1] 
    output_file_name = sys.argv[2]
# Call the main_maze_solver function with the provided input and output file names
    main_maze_solver(input_file_name, output_file_name)
