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
    words = {
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
                    for word in words:
                        end = i + len(word)
                        if end <= len(line) and line[i:end] == word:
                            numbers.append(words[word])
                            break
            sum += 10 * numbers[0] + numbers[-1]

    print("Part 2:", sum)

if __name__ == "__main__":
    main()