import argparse
import commands

url = ''
uri = ''
params = ''

def parse(complete_command):                                                                    #Parser für command
    complete_command = complete_command.split(' -')                                             #Command wird in den command und die args zerteilt
    command = complete_command[0]
    del complete_command[0]
    args = {}
    
    for i in range(len(complete_command)):                                                      #Die args werden aufgeteilt bsp.: '-u test' -> {'u': 'test'}
        try:
            args[complete_command[i].split(' ', 1)[0]] = complete_command[i].split(' ', 1)[1]
        except IndexError:
            args[complete_command[i].split(' ', 1)[0]] = ''
        
    args['command'] = command
    return args

def interpret_command(command):
    commands.url = url                      #Default url, uri, params werden weiter durchgereicht
    commands.uri = uri
    commands.params = params

    args = parse(command)

    if args['command'] == 'set':
        return commands.set(args)