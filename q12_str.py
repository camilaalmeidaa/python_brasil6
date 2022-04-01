def valida_telefone(tel):
    
    if ((tel[3] == '-') and (len(tel) == 8)):
        
        tel_com_tres = '3' + str(tel)

        tel_novo = tel_com_tres [0:4] + tel_com_tres [5:]
        
        
        print("Valida e corrige número de telefone")
        print("Telefone:",tel)
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        print("Telefone corrigido sem formatação:", tel_novo)
        print("Telefone corrigido com formatação:", tel_com_tres)
    
    elif ((tel[3] != '-') and (len(tel) == 7)):
        
        tel_com_tres = '3' + str(tel)
        
        tel_com_formatacao = tel_com_tres [0:4] + '-' + tel_com_tres [4:]
        
        print("Valida e corrige número de telefone")
        print("Telefone:",tel)
        print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.")
        print("Telefone corrigido sem formatação:", tel_com_tres)
        print("Telefone corrigido com formatação:", tel_com_formatacao)
    
    
    else:
        
        print("Número válido.")
        
        