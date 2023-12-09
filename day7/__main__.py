from collections import Counter
import bisect

def main():
    part1()
    part2()

class Hand:
    def __init__(self, cards, bid, card_type):
        self.cards = cards
        self.bid = bid
        self.card_type = card_type

    def __lt__(self, other):
        if self.card_type == other.card_type:
            for card, other_card in zip(self.cards, other.cards):
                if card != other_card:
                    return card < other_card
            return True
        return self.card_type < other.card_type

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
    card_list = []
    letter_map = {
        "T": "B",
        "J": "1",
        "K": "R",
        "A": "Z",
    }

    with open("day7/input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            [cards, bid] = line.split(" ")
            cards = cards.strip()
            bid = int(bid.strip())

            for old, new in letter_map.items():
                cards = cards.replace(old, new)
                
            counter = Counter(cards)
            joker_count = counter["1"]
            del counter["1"]
            counter_list = list(counter.most_common())
            card_type = (5 - len(counter_list))
            if card_type < 5:
                card_type += counter_list[0][1] + joker_count
            else:
                card_type += 4

            current_hand = Hand(cards, bid, card_type)
            bisect.insort_right(card_list, current_hand)

    score = 0
    for i, card in enumerate(card_list):
        score += (i + 1) * card.bid
        
    print("Part 2:", score)

if __name__ == "__main__":
    main()