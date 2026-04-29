import random
from art import logo


def deal_card(deck):
    """Returns a random card from the deck and remove it."""
    card = random.choice(deck)
    deck.remove(card)
    return card


def calculate_score(hand):
    """Take a list of cards and return the score calculated from cards."""
    score = 0
    for card in range(len(hand)):
        if hand[card] == "J" or hand[card] == "Q" or hand[card] == "K":
            score += 10
        elif hand[card] == "A":
            score += 11
        else:
            score += hand[card]
    if len(hand) == 2 and score == 21:
        return "Blackjack"
    elif "A" in hand and score > 21:
        score -= 10
    return score


def compare(ps, cs):
    if cs == "Blackjack":
        return "Computer Win!"
    elif ps == "Blackjack":
        return "Player win!"
    elif ps == cs:
        return "Draw"
    elif cs > ps and cs <= 21 or ps > 21:
        return "Computer Win!"
    elif ps > cs and ps <= 21 or cs > 21:
        return "Player Win!"


def game_round():
    deck = [
        "A",
        "A",
        "A",
        "A",
        2,
        2,
        2,
        2,
        3,
        3,
        3,
        3,
        4,
        4,
        4,
        4,
        5,
        5,
        5,
        5,
        6,
        6,
        6,
        6,
        7,
        7,
        7,
        7,
        8,
        8,
        8,
        8,
        9,
        9,
        9,
        9,
        10,
        10,
        10,
        10,
        "J",
        "J",
        "J",
        "J",
        "Q",
        "Q",
        "Q",
        "Q",
        "K",
        "K",
        "K",
        "K",
    ]
    player_hand = []
    computer_hand = []
    for n in range(2):
        computer_hand.append(deal_card(deck))
        player_hand.append(deal_card(deck))
    game_over = False
    print(logo)
    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(
            f"""
Computer hand: [{computer_hand[0]}, ?]
Player hand: {player_hand} | {player_score}"""
        )
        if (
            computer_score == "Blackjack"
            or player_score == "Blackjack"
            or player_score > 21
        ):
            game_over = True
            break
        else:
            want_card = input("Type 'y' for draw a card or 'n' for pass: ")
            if want_card.lower() == "y":
                player_hand.append(deal_card(deck))
            else:
                game_over = True
                while computer_score < 17 and computer_score != "Blackjack":
                    computer_hand.append(deal_card(deck))
                    computer_score = calculate_score(computer_hand)

    result = compare(ps=player_score, cs=computer_score)
    print(
        f"""
Computer hand: {computer_hand} | {computer_score}
Player hand: {player_hand} | {player_score}
{result}"""
    )
    restart = input("Type 'y' for play new game or 'n' for end: ")
    if restart.lower() == "y":
        print("\n" * 20)
        game_round()


game_round()
