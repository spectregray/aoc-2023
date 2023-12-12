from collections import defaultdict

def main():
    part1()
    part2()

def valid_indices(r, c, arr):
    return 0 <= r < len(arr) and 0 <= c < len(arr[0])

def part1():
    sum = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    with open("day03/input.txt", "r") as file:
        lines = file.readlines()

        # new line char needs to be removed
        for i, line in enumerate(lines):
            lines[i] = line.strip()

        for i, line in enumerate(lines):
            number = ""
            adjacent_to_symbol = False

            for j, character in enumerate(line.strip()):
                if character.isdigit():
                    number += character

                    if not adjacent_to_symbol:
                        for (r, c) in directions:
                            if valid_indices(r + i, c + j, lines) and not lines[r + i][c + j].isdigit() and lines[r + i][c + j] != ".": 
                                adjacent_to_symbol = True
                                break
                else:
                    if adjacent_to_symbol:
                        sum += int(number)
                    number = ""
                    adjacent_to_symbol = False
            if adjacent_to_symbol:
                sum += int(number)

    print("Part 1:", sum)

def part2():
    sum = 0
    gears = defaultdict(list) # key: tuple indicies of gear
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    with open("day03/input.txt", "r") as file:
        lines = file.readlines()

        # new line char needs to be removed
        for i, line in enumerate(lines):
            lines[i] = line.strip()

        for i, line in enumerate(lines):
            gear = None
            number = ""

            for j, character in enumerate(line.strip()):
                if character.isdigit():
                    number += character

                    for (r, c) in directions:
                        if valid_indices(r + i, c + j, lines) and lines[r + i][c + j] == "*": 
                            gear = (r + i, c + j)
                            break
                else:
                    if gear: 
                        gears[gear].append(int(number))
                    gear = None
                    number = ""
            
            if gear: 
                gears[gear].append(int(number))
    
    for adjacent_numbers in gears.values(): 
        if len(adjacent_numbers) == 2:
            sum += adjacent_numbers[0] * adjacent_numbers[1]

    print("Part 2:", sum)
    
if __name__ == "__main__":
    main()