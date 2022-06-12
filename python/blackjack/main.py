import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def get_one(cards):
    return random.choice(cards)


def fill_start(user, cards):
    for _ in range(2):
        card = get_one(cards)
        user.append(card)
    return user


currentHand = 'Player'
game_on = True
player_cards = fill_start([], cards)
dealer_cards = fill_start([], cards)


def main():
    game_on = True
    while game_on:
        print(f'Your sum is {sum(player_cards)}, willing to hit?')
        choice = input('yes / no \n')
        if choice == 'yes':
            player_cards.append(get_one(cards))
            dealer_sum = sum(dealer_cards)
            print(dealer_sum)
            if dealer_sum < 17:
                dealer_cards.append(get_one(cards))
            continue
        else:
            game_on = False

            finish_player = sum(list(player_cards))
            finish_dealer = sum(list(dealer_cards))

            if finish_player > 21:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('Dealer won , a bust!')
                game_on = False
                return
            elif finish_dealer > 21:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('Player won , a bust!')
                game_on = False
                return
            if finish_dealer == 21 and finish_player == 21:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('A draw!')
                game_on = False
                return
            elif finish_player == 21 and not finish_dealer == 21:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('Player won!')
                game_on = False
                return
            elif finish_player > finish_dealer and not finish_player > 21:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('Player won!')
                game_on = False
                return
            else:
                print(
                    f'Player have:{finish_player} and dealer have {finish_dealer}')
                print('Dealer won')
                game_on = False
                return


main()
