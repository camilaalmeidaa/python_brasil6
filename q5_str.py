def print_nome_escada_inverso():
    
    nome = input("Digite seu nome: ")
    
    nome_maiusculo = nome.upper()

    count = len(nome_maiusculo)
    
    while(count > 0):
        
        print(nome_maiusculo[0:count])
        
        count = count - 1

        

