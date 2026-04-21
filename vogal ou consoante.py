letra = input("Informe uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Entrada invalida. Digite apenas uma letra.")
elif letra in "aeiou":
    print(f"A letra '{letra}' e uma vogal.")
else:
    print(f"A letra '{letra}' e uma consoante.")
