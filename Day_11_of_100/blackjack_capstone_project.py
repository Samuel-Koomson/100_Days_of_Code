import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = random.choices(cards, k=2)
computer_card = random.choices(cards, k=2)
print(user_card)
print(computer_card)

ace = []

def deal_card():
    user_deal_card = random.choice(cards)
    computer_deal_card = random.choice(cards)
    user_card.append(user_deal_card)
    computer_card.append(computer_deal_card)
    
    if sum(user_card) or sum(computer_card) < 21:
        ace = cards[0]
    # print(ace)
    else:
        ace = 1

    # blackjack = 0
    # special_card = cards[:-4]
    # if ace == 11:
    #     for card in cards:
    #         if card == 10:
    #             blackjack = ace + card
    #             return 0
    # print(blackjack)
deal_card()


# calculate score funtion
def calculate_score(score):
    score = sum(score)
    print(score)

    blackjack = 0
    # special_card = cards[:-4]
    if ace == 11:
        for card in cards:
            if card == 10:
                blackjack = ace + card
                return 0
    print(blackjack)
    return score

calculate_score(user_card)
calculate_score(computer_card)
