lista = ["a","b","c","D"] 

for letters in lista:
    num_l = lista.index(letters) + 1 # index the letters and sum 
    print(f"Letters {num_l}: {letters}")
    