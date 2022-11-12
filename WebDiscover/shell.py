import interpret
import argparse
from colorama import Fore, Back, init

def run_shell():
    init(autoreset=True)
    response = {}
    values = {'url': '', 'uri': '', 'params': ''}
    command = ''
    while True:
        if values['url'] == '' and values['uri'] == '':
            command = input(Fore.GREEN + '[' + Fore.BLUE + 'nothing' + Fore.GREEN + ' ]>> ')
        else:
            command = input(Fore.GREEN + '[' + Fore.BLUE + values['url'] + Fore.YELLOW + values['uri'] + Fore.RED + values['params'] + Fore.GREEN + ' ]>> ')
        
        interpret.url = values['url']                                        #url, uri, params werden durchgereicht das sie überall verfügbar sind
        interpret.uri = values['uri']
        interpret.params = values['params']
        response = interpret.interpret_command(command)

        try:
            for i in response:                                              #Neue Werte werden übernommen
                values[i] = response[i]
        except TypeError:
            pass
        
run_shell()