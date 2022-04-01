def check_palindrome(word):
    
    if str(word) == str(word)[::-1] :
        
        print(word,": Palíndromo")
        
    else:
        
        print(word,": Não é Palíndromo")