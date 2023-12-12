"""
* Only runs in Python3
"""

def main():
    part1()
    part2()

def valid (x, y, row_len, col_len):
    return 0 <= x < row_len and 0 <= y < col_len

def part1():
    longest = 0
    visited = set()
    visit = []

    with open("day10/input.txt", "r") as file:
        lines = file.readlines()

        for row, line in enumerate(lines):
            if "S" in line:
                visit.append((row, line.index("S"), 0))
                break
        
        while visit: 
            print(visit)
            x, y, dist = visit[0] # unfortunately x is row, y is col
            if 0 <= x < len(lines) and 0 <= y < len(lines[0]):

                if (x, y) not in visited:
                    if dist > longest and lines[x][y] != ".":
                        longest = dist

                    match lines[x][y]:
                        case "F":
                            visit.append((x + 1, y, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "7":
                            visit.append((x, y - 1, dist + 1))
                            visit.append((x + 1, y, dist + 1))
                        case "J":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x, y - 1, dist + 1))
                        case "L":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "|":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x + 1, y, dist + 1))
                        case "-":
                            visit.append((x, y - 1, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "S":
                            sx, sy = x - 1, y
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "F" or lines[sx][sy] == "7" or lines[sx][sy] == "|":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x + 1, y
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "J" or lines[sx][sy] == "L" or lines[sx][sy] == "|":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x, y - 1
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "L" or lines[sx][sy] == "F" or lines[sx][sy] == "-":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x, y + 1
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "J" or lines[sx][sy] == "7" or lines[sx][sy] == "-":
                                    visit.append((sx, sy, dist + 1))
                        case _:
                            pass
                    visited.add((x, y))
            visit.pop(0)

    print("Part 1:", longest)

def part2():
    longest = 0
    visited = set()
    visit = []

    with open("day10/input.txt", "r") as file:
        lines = file.readlines()

        for row, line in enumerate(lines):
            if "S" in line:
                visit.append((row, line.index("S"), 0))
                break
        
        while visit: 
            print(visit)
            x, y, dist = visit[0] # unfortunately x is row, y is col
            if 0 <= x < len(lines) and 0 <= y < len(lines[0]):

                if (x, y) not in visited:
                    if dist > longest and lines[x][y] != ".":
                        longest = dist

                    match lines[x][y]:
                        case "F":
                            visit.append((x + 1, y, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "7":
                            visit.append((x, y - 1, dist + 1))
                            visit.append((x + 1, y, dist + 1))
                        case "J":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x, y - 1, dist + 1))
                        case "L":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "|":
                            visit.append((x - 1, y, dist + 1))
                            visit.append((x + 1, y, dist + 1))
                        case "-":
                            visit.append((x, y - 1, dist + 1))
                            visit.append((x, y + 1, dist + 1))
                        case "S":
                            sx, sy = x - 1, y
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "F" or lines[sx][sy] == "7" or lines[sx][sy] == "|":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x + 1, y
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "J" or lines[sx][sy] == "L" or lines[sx][sy] == "|":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x, y - 1
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "L" or lines[sx][sy] == "F" or lines[sx][sy] == "-":
                                    visit.append((sx, sy, dist + 1))
                            sx, sy = x, y + 1
                            if valid(sx, sy, len(lines), len(lines[0])):
                                if lines[sx][sy] == "J" or lines[sx][sy] == "7" or lines[sx][sy] == "-":
                                    visit.append((sx, sy, dist + 1))
                        case _:
                            pass
                    visited.add((x, y))
            visit.pop(0)

    print("Part 2:", longest)

if __name__ == "__main__":
    main()