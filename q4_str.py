def print_nome_escada():
    
    nome = input("Digite seu nome: ")
    
    nome_maiusculo = nome.upper()

    for i in range(0,len(nome_maiusculo)+1):
        
        print(nome_maiusculo[:i])

        

