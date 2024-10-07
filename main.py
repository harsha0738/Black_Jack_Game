import random
import art

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_s, c_s):
    if u_s == c_s:
        return "It's a Draw 🥲"
    elif c_s == 0:
        return "You loose. 🤦‍♂️"
    elif u_s == 0:
        return "Hurrayyy You won. 😁"
    elif u_s > 21:
        return "You lost coz you went over. 😭"
    elif c_s > 21:
        return "You won coz computer went over.😁"
    elif u_s > c_s:
        return "You won.😎"
    else:
        return "you lost. 😒"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards are : {user_cards}, current score is {user_score}")
        print(f"computer's first card is {computer_cards[0]}" )

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("do you want to draw another card? type 'y' or 'n'.")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your cards are : {user_cards}, and your score is {user_score}")
    print(f"compter's cards are : {computer_cards}, and computer score is {computer_score}")
    print(compare(user_score, computer_score))

while input("Type 'y' to play the game again or type 'n' to pass? : ") == "y":
    print("\n" * 20)
    play_game()







