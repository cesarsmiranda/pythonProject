# Cria uma lista vazia para armazenar alienigenas

aliens = []

#cria 30 alienigenas verdes
for alien_number in range(30):
        new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
        aliens.append(new_alien)

# mostra os 5 primeiros alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")

#mostra quantos alienigenas foram criados
print("Total number of aliens: " + str(len(aliens)))

