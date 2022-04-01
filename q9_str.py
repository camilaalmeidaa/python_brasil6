def checa_cpf():
    
    cpf = input("Digite o CPF no formato (xxx.xxx.xxx-xx): ")
    
    if ((cpf[3] != '.') or (cpf[7] != '.') or (cpf[11] != '-')):
        
        print("CPF inválido. Digite no formato (xxx.xxx.xxx-xx).")
    
    else:
        
        print("CPF válido.")