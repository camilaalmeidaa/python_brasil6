def compare_str(*strings):
    
    for i in range(len(strings)):
        
        print("String", i+1,":", strings[i])
    
    for i in range(len(strings)):
        
        print("Tamanho de", strings[i],":", len(strings[i]),"caracteres")
        
    if(len(strings[0]) == len(strings[1])):
        
        print("As duas strings são de tamanhos iguais.")
    
    else:
        
        print("As duas strings são de tamanhos diferentes.")
        
    
    if(strings[0] == strings[1]):
        
        print("As duas strings possuem conteúdo igual.")
    
    else:
        
        print("As duas strings possuem conteúdo diferente.")

        
def compare_two_str(str1, str2):
    
    
    compare_str(str1, str2)