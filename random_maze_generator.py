import sys
import random

def random_arrow(color):
    directions = ['N', 'E', 'S', 'W', 'NE', 'SE', 'SW', 'NW']
    return f"{color}-{random.choice(directions)}"

def generate_maze(rows, cols):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if r == rows - 1 and c == cols - 1:
                row.append('O')
            else:
                color = random.choice(['R', 'B'])
                row.append(random_arrow(color))
        maze.append(row)
    return maze

def write_maze(maze, output_file):
    with open(output_file, 'w') as f:
        f.write(f"{len(maze)} {len(maze[0])}\n")
        for row in maze:
            f.write(' '.join(row) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python random_maze_generator.py ROWS COLS OUTPUT_FILE")
        sys.exit(1)
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    output_file = sys.argv[3]
    maze = generate_maze(rows, cols)
    write_maze(maze, output_file)
    print(f"Random maze ({rows}x{cols}) written to {output_file}")
