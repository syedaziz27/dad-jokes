import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = colored(figlet_format('DAD JOKE 3000!'), color='cyan')
print(header)


def get_joke():
    user_input = input('What kind of joke would you like? \n')
    url = 'https://icanhazdadjoke.com/search'

    res = requests.get(
        url,
        headers={'Accept': 'application/json'},
        params={'term': user_input}
    ).json()

    num_jokes = res['total_jokes']
    results = res['results']

    if num_jokes == 1:
        print(f'I\'ve got one {user_input} joke! Here it is:')
        print(colored(choice(results)['joke'], color='magenta'))
    if num_jokes > 1:
        print(f'I\'ve got {num_jokes} {user_input} jokes! Here\'s one:')
        print(colored(choice(results)['joke'], color='magenta'))
    if num_jokes == 0:
        print(f'Sorry, I don\'t have any {user_input} jokes.')

    another_joke = input('Would you like another one? (y/n) \n')

    if another_joke is 'y':
        get_joke()
    elif another_joke is 'n':
        print(colored('See Ya!', color='blue'))


get_joke()
