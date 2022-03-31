def print_name_reverse():
    
    nome = input("Digite seu nome: ")
    
    nome_maiusculo = nome.upper()
    
    nome_reverse = nome_maiusculo[::-1]
    
    for i in range(len(nome_reverse)):
        
        print(nome_reverse[i])