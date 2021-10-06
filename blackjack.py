import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]

TEN_CARDS = ["jack", "queen", "king"]

hand = []


def count_numbers_of_cards(hand, casino=False):
    sum_of_cards = 0
    for i in hand:
        if i in TEN_CARDS:
            sum_of_cards += 10
        elif i == 'ace':
            if casino:
                ace_value = random.choice([1, 11])
            else:
                ace_value = int(input("You have an ace. IS it 1 or 11? \n"))
            sum_of_cards += ace_value
        else:
            sum_of_cards += i
    return sum_of_cards


def get_result(hand):
    casino_hand = [random.choice(deck) for x in range(4)]
    print(casino_hand)
    casino = count_numbers_of_cards(casino_hand, True)
    print(f'Casino\'s score: {casino}')
    player = count_numbers_of_cards(hand)
    print(f'Your score is {player}')
    if (player > 21 or casino == 21) or (21 > casino > player and player < 21):
        print("You lose")
        return
    if (player == 21 or casino > 21) or (21 > player > casino and casino < 21):
        print("You win!")
        return
    else:
        print("It's a draw")


if __name__ == '__main__':
    while True:
        if hand:
            print(f"Your cards are: {hand}")
        step = input("Write in your next step: ")
        if step == "start":
            if not hand:
                hand.append(random.choice(deck))
                hand.append(random.choice(deck))
            else:
                print("You've already started")
        elif step == "hit":
            new_card = random.choice(deck)
            print("Your card is: ", new_card)
            hand.append(new_card)
        elif step == "stand":
            break
        elif not step:
            print("Write down your step")
        else:
            print("Write down 'start'")
    get_result(hand)
