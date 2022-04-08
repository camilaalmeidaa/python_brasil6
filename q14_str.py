def leet_translator():
    
    texto = input("Digite um texto: ")

    leet_traduzido = texto

    leet = {'e': '3','s': '5','a': '4','you': 'j00','o': '0','E': '3','S': '5','A': '4','You': 'j00',
    'O': '0','t': '7','T': '7','i': '1','I': '1',}

    for x, y in leet.items():
        
        leet_traduzido = leet_traduzido.replace(x, y)

    print(texto,"=",leet_traduzido)
