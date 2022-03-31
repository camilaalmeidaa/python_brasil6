def calcular_ocorrencias(string):
    
    count_espacos = 0
    
    vogais = ['a','e','i','o','u']
    
    count_vogais = 0
    
    
    for i in range(0, len(string)): 
        
        if string[i] == " ": 
          
            count_espacos += 1
        
        elif string[i] in vogais:
            
            count_vogais += 1
    
    print(count_espacos,"espaços e",count_vogais,"vogais [a,e,i,o,u].")
    
        