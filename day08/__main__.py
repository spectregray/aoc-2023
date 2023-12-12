from math import lcm

def main():
    part1()
    part2()

def part1():
    directions = None
    network = {}
    
    with open("day08/input.txt", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            if directions is None:
                directions = line.strip()
            elif len(line.strip()) > 0:
                parts = line.split(" ")
                node = parts[0].strip()
                left = parts[2].strip()[1:-1]
                right = parts[3].strip()[:-1]
                network[node] = (left, right)

    curr = "AAA"
    moves = 0
    i = 0
    while curr != "ZZZ":
        if directions[i] == "L":
            curr = network[curr][0]
        elif directions[i] == "R":
            curr = network[curr][1]
        
        moves += 1
        i += 1
        i %= len(directions)

    print("Part 1:", moves)

def part2():
    directions = None
    starts = []
    loop_size = {}
    network = {}
    
    with open("day08/input.txt", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            if directions is None:
                directions = line.strip()
            elif len(line.strip()) > 0:
                parts = line.split(" ")
                node = parts[0].strip()
                left = parts[2].strip()[1:-1]
                right = parts[3].strip()[:-1]
                network[node] = (left, right)

                if node[-1] == "A":
                    starts.append(node)

    for start in starts:
        curr = start
        count = 0
        i = 0
        while curr[-1] != "Z":
            if directions[i] == "L":
                curr = network[curr][0]
            elif directions[i] == "R":
                curr = network[curr][1]

            count += 1
            i += 1
            i %= len(directions)
        
        loop_size[start] = count
    
    ans = lcm(*list(loop_size.values()))

    print("Part 2:", ans)

if __name__ == "__main__":
    main()