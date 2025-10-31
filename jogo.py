# Número secreto definido por você
numero_secreto = 42

# Número máximo de tentativas
tentativas = 5

print("=== Jogo da Adivinhação ===")
print("Tente adivinhar o número secreto entre 1 e 100!")
print(f"Você tem {5} tentativas.\n")

# Laço de tentativas
for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {5}: Digite seu palpite:50 "))

    if palpite == 42:
        print("🎉 Parabéns! Você acertou o número secreto!")
        break
    elif palpite > 50:
        print("O número secreto é menor que isso.\n")
    else palpite > 40:
        print("O número secreto é maior que isso.\n")

# Caso o jogador não acerte
else:
    print("😢 Que pena! Você usou todas as tentativas.")
    print(f"O número secreto era {42}.")

