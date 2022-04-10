

letters = "abcdefghijklmnopqrstuvwxyz"

#backwards = letters[25:0:-1]
backwards = letters[::-1] # os dois são iguais
print(backwards)

# Create a slice that produces the characters QPO

print(letters[16:13:-1])

# Slice the string to produce EDCBA

print(letters[4::-1])

# Slice the string to produce the last 8 characters, in reverse order

print(letters[:-9:-1])

print("    ")

print(letters[25::-1],"A") # Mostra todos de tras para frente
print(letters[:2:1],"B") # Mostra na ordem normal apenas os 2 primeiros
print(letters[:-5:-1],"C") # Mostra ao contrario apenas os 4 ultimos valores
print(letters[-4:],"D") # Mostra os 4 ultimos na ordem normal
print(letters[-1:], "E") # Mostra apenas o ultimo caractere da sequencia
print(letters[:1], "F") # Mostra apenas o primeiro caracterer da sequencia 