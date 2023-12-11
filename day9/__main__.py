"""
Summary: Given one line, calculate all its histories, then traverse them in
reverse, taking the last element of each history to calculate the answer.
"""

def main():
    part1()
    part2()

def part1():
    ans = 0

    with open("day9/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(" ")
            histories = [[int(part) for part in parts]]

            while histories:
                last = histories[-1]
                if last[-1] == 0:
                    break
                
                new = [] 
                prev = None
                for l in last: 
                    if prev is not None:
                        diff = l - prev
                        new.append(diff) 
                    prev = l
                histories.append(new)

            prev_last = histories[-1][-1]
            for history in list(reversed(histories))[1:]:
                prev_last += history[-1]

            ans += prev_last

    print("Part 1:", ans)

def part2():
    ans = 0

    with open("day9/input.txt", "r") as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(" ")
            histories = [[int(part) for part in parts]]

            while histories:
                last = histories[-1]
                if last[-1] == 0:
                    break
                
                new = [] 
                prev = None
                for l in last: 
                    if prev is not None:
                        diff = l - prev
                        new.append(diff) 
                    prev = l
                histories.append(new)

            prev_last = histories[-1][0]
            for history in list(reversed(histories))[1:]:
                print(history)
                prev_last = history[0] - prev_last

            ans += prev_last

    print("Part 2:", ans)

if __name__ == "__main__":
    main()