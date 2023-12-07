from collections import Counter
import bisect

def main():
    part1()
    part2()

class Hand:
    def __init__(self, cards, bid, hand_type):
        self.cards = cards
        self.bid = bid
        self.hand_type = hand_type

    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            for card, other_card in zip(self.cards, other.cards):
                if card != other_card:
                    return card < other_card
            return True
        return self.hand_type < other.hand_type

def part1():
    card_list = []
    letter_map = {
        "T": "B",
        "J": "L",
        "K": "R",
        "A": "Z",
    }

    with open("day7/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            [cards, bid] = line.split(" ")
            cards = cards.strip()
            for old, new in letter_map.items():
                cards = cards.replace(old, new)
            bid = int(bid.strip())
            count = list(Counter(cards).most_common())
            card_type = (5 - len(count)) + count[0][1]

            current_hand = Hand(cards, bid, card_type)
            bisect.insort_right(card_list, current_hand)

    score = 0
    for i, card in enumerate(card_list):
        score += (i + 1) * card.bid

    print("Part 1:", score)

def part2():
    pass

if __name__ == "__main__":
    main()