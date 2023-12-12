def main():
    part1()
    part2()

def part1():
    sum = 0
    max_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    with open("day2/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            subsets = line[line.index(":") + 1:].split(";")
            valid_game = True

            for subset in subsets:
                cubes = subset.strip().split(", ")

                for cube in cubes:
                    cube_values = cube.strip().split(" ")
                    count, color = int(cube_values[0]), cube_values[1]
                    if count > max_cubes[color]:
                        valid_game = False
                        break

            if valid_game:
                sum += int(line[line.index(" ") + 1: line.index(":")])

    print("Part 1:", sum)

def part2():
    sum = 0

    with open("day2/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            subsets = line[line.index(":") + 1:].split(";")
            max_cubes = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for subset in subsets:
                cubes = subset.strip().split(", ")

                for cube in cubes:
                    cube_values = cube.strip().split(" ")
                    count, color = int(cube_values[0]), cube_values[1]
                    if count > max_cubes[color]:
                        max_cubes[color] = count

            power = None
            for count in max_cubes.values():
                if power is None:
                    power = count
                else:
                    power *= count
            
            sum += power


    print("Part 2:", sum)
    
if __name__ == "__main__":
    main()