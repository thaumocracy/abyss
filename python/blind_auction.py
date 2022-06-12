def main():
    bidders = []
    ready = False
    while not ready:
        print('Welcome to our auction. Please enter you name and bid')
        bidder = get_input()
        bidders.append(bidder)
        next_bidder = input('Is there another bidders left? yes \ no \n')
        if next_bidder == 'no':
            ready = True

    if ready:
        winner = calculate_winner(bidders)
        name = winner['name']
        bid = winner['bid']
        print(f'The winner is {name} with bid of {bid}')


def get_input():

    name = input('Enter your name: \n')
    bid = int(input('Enter your bid: \n'))

    return {
        "name": name,
        "bid": bid
    }


def calculate_winner(array):
    winner = {
        'name': None,
        'bid': 0
    }

    for bidder in array:
        if bidder['bid'] > winner['bid']:
            winner = bidder

    return winner


main()
