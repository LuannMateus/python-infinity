from random import randint

random_number = randint(1, 10)

user_number = input("Digite um número: ")

if random_number == user_number:
    print(f"O número era {random_number}. Parabéns!")
else:
    print("Você errou!")