#Hier werden die Command definiert die in interpret.py aufgerufen werden
#TODO: url parsing flexibeler dass man in parse_url auswählen kann was man parsen möchte also z.b. nur params oder nur uri
#-> so muss nicht so viel wiederholt werden. Siehe command "set" auswerten der args

import re

url = ''                #Wenn nichts anderes angegeben in den args dann werden wenn nötig die Daten von hier genommen
uri = ''
params = ''

def parse_url(complete_url):                                               #URL wird in erster Teil der URL: http://irgendwas.de, Uri: /irgendwas/lol und Parametern: ?test=test geparsed
    response = {}                                                       #Check URL
    parsed = re.findall('https?://[üöäßA-Z0-9a-z._-]*', complete_url)
    if parsed == []:
        print('[-]invalid URL')
        return {}
    response['url'] = parsed[0]
    complete_url = ''.join(list(complete_url)[len(parsed[0]):])

    parsed = re.findall('/[üöäßA-Z0-9a-z./_-]*', complete_url)             #Check URI
    
    if parsed == []:                                                   #Fallse URI leer wird response zurückgegeben
        print('[-]No or No valid URI specified')
        return response
    if parsed[0] == '/':                                                #Falls URI nur / ist wird dieser verworfen
        return response

    if parsed[0][len(parsed[0])-1] == '/':
        parsed = ''.join(list(parsed[0])[:len(parsed[0])-1])         #Falls am Ende der URI noch ein / ist wird dieser entfernt
        complete_url = ''.join(list(complete_url)[len(parsed)+1:])
    else:
        parsed = parsed[0]
        complete_url = ''.join(list(complete_url)[len(parsed):])
    response['uri'] = parsed
    
    response['params'] = complete_url                                   #Wenn noch etwas übrig ist wird dieser noch als Parameter gewertet und angehangen
    return response

def set(args):                                                         #args = geparster Command
    response = {}
    if 'all' in args:                                   #args werden ausgewertet
        if args['all'] == '':
            print('[-]invalid URL')
        else:
            if 'all' in args:
                return parse_url(args['all'])
            else:
                return parse_url(args['a'])
    
    if 'url' in args:
        if args['url'] == '':
            print('[-]invalid URL')
        else:                                                                       
            parsed = re.findall('https?://[üöäßA-Z0-9a-z._-]*', args['url'])
            if parsed == []:
                print('[-]invalid URL')
                return {}
            response['url'] = parsed[0]
    
    if 'uri' in args:
        parsed = re.findall('/[üöäßA-Z0-9a-z./_-]*', args['uri'])             
    
        if parsed == []:                                                   
            print('[-]No or No valid URI specified')
            return response
        if parsed[0] == '/':                                                
            return response

        if parsed[0][len(parsed[0])-1] == '/':
            parsed[0] = ''.join(list(parsed[0])[:len(parsed[0])-1])         
    
        response['uri'] = parsed[0]

    if 'params' in args:
        response['params'] = args['params']                                  #!!!!!!!!!!!!Params wird noch nicht geparsed!!!!!!!!!!!!!!!!!

    else:
        print('[-]This argument does not exist')
    return response