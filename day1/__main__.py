def main():
    part1()
    part2()

def part1():
    sum = 0 

    with open("day1/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            numbers = []

            for character in line: 
                if character.isdigit():
                    numbers.append(int(character))
            
            sum += 10 * numbers[0] + numbers[-1]

    print("Part 1:", sum)

def part2():
    sum = 0
    text_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    with open("day1/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            numbers = []

            for i, character in enumerate(line):
                if character.isdigit():
                    numbers.append(int(character))
                else:
                    for text in text_to_int:
                        end = i + len(text)
                        if end <= len(line):
                            if line[i:end] == text:
                                numbers.append(text_to_int[text])
                                break
            sum += 10 * numbers[0] + numbers[-1]

    print("Part 2:", sum)

if __name__ == "__main__":
    main()